from django.shortcuts import get_object_or_404, redirect, render
from .forms import(FamilyMemberFormSet,  CostCenterForm,CostCenterFormUpdate 
,CurrencyFormUpdate,CurrencyForm  )
from Finance.models import  *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import CostCFilter,CurrencyFilter
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ValidationError
from django.http import JsonResponse, request
from django.db.models import Sum
from Finance.filters import TranMainFilter
from django.core.exceptions import ValidationError  
from django.forms.utils import ErrorList
from itertools import count
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from Finance.forms import InvoiceForm
from templated_docs import fill_template
from templated_docs.http import FileResponse
from Finance.utilspdf import render_to_pdf
from django.views.generic import View
from django.template.loader import get_template

from datetime import date
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from .forms import WeatherForm
from .models import Town, Weather
 
 

def Geo(request):
        return render(request, 'Finance/Geo.html')

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('Finance/pdf/invoice.html')
        context = {
            'today': 2, 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        html=template.render(context)
        pdf = render_to_pdf('Finance/pdf/invoice.html', context)
        if pdf:
            response=HttpResponse(pdf, content_type='application/pdf')
            filename="Invoice_%s.pdf" %("12345623")
            content="inLine;filename='%s'" %(filename)
            response['Content-Disposition']=content
            return response
        return HttpResponse("Not found")

# def Generate_view(request, *args, **kwargs):
#         template = get_template('Finance/invoice.html')
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('pdf/invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('Finance/pdf/invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('Finance/pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

def invoice_view(request):
    try:

        form = InvoiceForm(request.POST)

        if form.is_valid():
            doctype = form.cleaned_data['format']
            print('form.cleaned_data',form.cleaned_data)
            filename = fill_template('Finance/invoice.odt', form.cleaned_data,output_format=doctype)
            visible_filename = 'invoice.{}'.format(doctype)

            return FileResponse(filename, visible_filename)
        else:
            return render(request, 'Finance/form.html', {'form': form})
    except IntegrityError as e: 
        print('error',e)  
#post
def Post_(request):
    id = request.GET.get('id', None)
    TranMain = TranTableMain.objects.get(id=id)
    TranMain.Post=True
    TranMain.save()
    data = {
             'is_taken': TranTableMain.objects.filter(id__iexact=id).exists()
           }
    return JsonResponse(data)

#chart of account 
def index(request):
        return render(request, 'Finance/index.html')


def get(request):
    accounts = list(Account.objects.values())
    return JsonResponse(accounts, safe=False)


def create(request):
    try:
        accountcode = request.POST['accountcode']
        pId = request.POST['pId']
        name = request.POST['name']
        mainaccount = request.POST['mainaccount']

        account = Account(pId=pId if pId != 'null' and pId != '' and pId != 'undefined' else None , name=name, accountcode=accountcode,mainaccount=mainaccount)
        account.save()
        return JsonResponse({'id': account.id}, safe=False);
    except (KeyError):
        return HttpResponseBadRequest()


def update(request):
    try:
        id = request.POST['id']

        account = Account.objects.get(id=id)

        account.pId = request.POST['pId'] if  request.POST['pId'] != 'null' and request.POST['pId'] != '' else None
        account.name = request.POST['name']
        account.accountcode = request.POST['accountcode']

        account.save()
        return JsonResponse(True, safe=False);
    except (KeyError,Account.DoesNotExist):
        return HttpResponseBadRequest()


def delete(request):
    try:
        id = request.POST['id']

        account = Account.objects.get(id=id)
        account.delete_r()
        return JsonResponse(True, safe=False);
    except (KeyError, Account.DoesNotExist):
        return HttpResponseBadRequest()


#ReceiptForm
# class ArticaleListview(listview):
#     template_name = 'Finance/test/profile_list.html'
#     queryset= Profile.objects.all()

# class ArticalDetialsview(DeleteView):
#     template_name = 'Finance/test/profile_list.html'
#     def get_object_or_404(self):
#         id_=self.kwargs.get("id")
#         return get_object_or_404(Profile,id=id_) 

# def list(request):
      
     
#     return render(request, 'Finance/index.html')
# class ArticaleUpdateView(UpdateView):
#     template_name=''
#     form_class=AritcalModelForm
#     def get_objects(self):
#         id_=self.kwargs.get("id")
#         return get_object_or_404(Profile,id=id_)
#     def form_valid(self,form):
#         return super().form_valid(from)   

# class ArticaleDeleteView(DeleteView):
    #     template_name=''
#     
#     def get_objects(self):
#         id_=self.kwargs.get("id")
#         return get_object_or_404(Profile,id=id_)
#     def get_success_url(self):
#         return  revers('app_name:articl-list')
 

# class ProfileList(ListView):
def ProfileList(request):
   
    item_list = TranTableMain.objects.all().order_by('id') 
    myFilter = TranMainFilter(request.GET, queryset=item_list)
    form = myFilter.qs 

    page = request.GET.get('page', 1)

    paginator = Paginator(form, 7)
    try:
        form = paginator.page(page)
    except PageNotAnInteger:
         form = paginator.page(1)
    except EmptyPage:
         form = paginator.page(paginator.num_pages)
    context={'form': form ,'myFilter':myFilter}
    return render(request, 'Finance/trantablemain_list.html',context)


class ProfileCreate(CreateView):
    model = TranTableMain
    fields =['notebookNum', 'description','TranDate','Post']


class ProfileFamilyMemberCreate(CreateView):
    model = TranTableMain # this main table
    # template_name=''
    fields =  ['notebookNum', 'description','TranDate','Post'] #['first_name', 'last_name']
    success_url = reverse_lazy('profile-list')
    
    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['owner'] = self.request.user
    #     return initial

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
         
        if self.request.POST:
            # print('is request ===={}'.format(self.request.POST)
            # print('FamilyMemberFormSet(self.request.POST)===={}'.format(FamilyMemberFormSet(self.request.POST))
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        
        return data
    

    @transaction.atomic  
    def form_valid(self, form):
         

        # for for_ in form:
        #     print(for_)
        try:
                context = self.get_context_data()
                familymembers2 = context['familymembers']
                
            # with transaction.atomic(): 
                
                # form.instance.created_by=self.request.user
                self.object = None

                if familymembers2.is_valid():
                    Totaldebit=0.00
                    TotalCredit=0.00
                    TotalCr=0.00
                    Totalde=0.00
                    for s in familymembers2.forms:
                        
                        if (s.cleaned_data.get('debit')) and not(s.cleaned_data.get('DELETE', False)):
                            Totalde   =  s.cleaned_data.get('debit')
                        if (s.cleaned_data.get('credit')) and not(s.cleaned_data.get('DELETE', False)):
                            TotalCr   =  s.cleaned_data.get('credit')

                        Totaldebit    = Totaldebit + float(Totalde)
                        TotalCredit    = TotalCredit + float(TotalCr)
                        TotalCr=0.00
                        Totalde=0.00
                    if not (Totaldebit == TotalCredit) or (Totaldebit + TotalCredit)==0:

                        messages.add_message(self.request, messages.INFO , "القيد غير متزن او  قم بادخال تفاصيل القيد")
                        return self.form_invalid(form)

                             
                    tran_Max=TranTableMain.objects.aggregate(Tran_max=Max('TranNo'))
                    TranNo=0
                    if  tran_Max['Tran_max'] is not None  :
                         TranNo     =   tran_Max['Tran_max']+1
                    else:
                        year=yearTBL.objects.first()
                        TranNo     =  '{0}{1}{2}{3}'.format(str(year.CurentYear)[2:],  1, str('0000'),1)

                    if TranNo is None or TranNo <1000 :
                        messages.add_message(self.request, messages.INFO , "يوجد خطأ في رقم القيداعد ادخال السند")
                        return self.form_invalid(form)    
                    # return self.form_invalid(form) 

                    for f in familymembers2.forms:
                        amount=0.00
                        # print(dir(f))
                        # print('- ---len--- 1---------------------------dir')
                        # print(f.cleaned_data.get('debit'))
                        # print('len(f.cleaned_data)issa is',len(f.cleaned_data))
                        
                      
                        # if  f.cleaned_data.get('DELETE', True):
                           
                        debit = f.cleaned_data.get('debit') # this come from form 
                        credit = f.cleaned_data.get('credit')
                       
                        # print('debit is {} credit {}'.format(debit,credit))   
                        if credit and debit:
                            messages.add_message(self.request, messages.INFO, "!!فضلا ادخل فقط الجانب الدائن او المدين في السطر الواحد")
                            return self.form_invalid(form)
                            #  self.form_invalid(form)
                             #raise ValidationError("!!فضلا ادخل فقط الجانب الدائن او المدين في السطر الواحد")
                        
                             
                        
                        elif  len(f.cleaned_data)==0:
                            continue
                     
                        elif len(f.cleaned_data)>0 and    (credit ==''   and debit ==''  ):
                            messages.add_message(self.request, messages.INFO, "!!لابد من ادخال الجانب الدائن او المدين")
                            return self.form_invalid(form)
                            # raise ValidationError("!!لابد من ادخال الجانب الدائن او المدين",not(credit  and debit  ))
                        
                        # return self.form_invalid(form) 
                        elif debit:
                            amount = float(debit)
                            debit=None
                        elif credit:
                            amount = -1 * float(credit)
                            credit=None
                        elif (debit is None) and (credit is None) and not (f.cleaned_data.get('DELETE', False) ):
                            messages.add_message(self.request, messages.INFO, "ادخل الجانب الدائن اوالمدين على الاقل")
                            return self.form_invalid(form)
                            #  return self.form_invalid(form) 

 
                        f.instance.TranAmount = amount
                        f.instance.TranNo =  TranNo
                    self.object            =None
                    self.object            = form.save(commit=False)
 
                    self.object.TranNo      = TranNo
                   
                    self.object.added_by    = self.request.user
                    self.object.Cate        =  self.kwargs['cat']
                    self.object.branchName = branch.objects.only('id').get(id= 1)
                    familymembers2.instance =  self.object
                    self.object.save()
                    count= familymembers2.save()
                    if len(count) <2 or self.kwargs['cat'] =='':
                        transaction.set_rollback(True)
                        messages.add_message(self.request, messages.INFO, "اعد ادخال القيد حدث خطأ اثناء حفظ القيد")
                        return self.form_invalid(form)
                    # transaction.savepoint_commit(sid)
                 
                     

                else:
                    transaction.set_rollback(True)
                    messages.add_message(self.request, messages.INFO,  familymembers2.errors)
                    return self.form_invalid(form) 
                    # raise ValidationError("أتمم ادخال تفاصيل القيد بصورة صحيحة")
                
        except IntegrityError as e:
                transaction.set_rollback(True)
                messages.add_message(self.request, messages.INFO,  e)
                return self.form_invalid(form) 
        try:
            return super(ProfileFamilyMemberCreate, self).form_valid(form)
        except IntegrityError as e:
            transaction.set_rollback(True)
            messages.add_message(self.request, messages.INFO,  e)
            return self.form_invalid(form) 


class ProfileUpdate(UpdateView):
    model = TranTableMain
    success_url = '/'
    fields =['notebookNum', 'description','TranDate']


class ProfileFamilyMemberUpdate(SuccessMessageMixin, UpdateView):
    model = TranTableMain
    fields = ['notebookNum', 'description','TranDate','Post']
    success_url = reverse_lazy('profile-list')
    # success_message = 'List successfully saved!!!!'
     

    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #         calculated_field=self.object.calculated_field,
    #     )

     
    
    def get_initial(self):
        initial =  super(ProfileFamilyMemberUpdate, self).get_initial()
      
        # obj = self.object

        # print(obj)

        # if obj.TranAmount > 0:
        #     initial['debit'] = obj.TranAmount
        #     initial['credit'] = 0
        # else:
        #     initial['credit'] = obj.TranAmount
        #     initial['debit'] = 0
        
        return initial

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST, instance=self.object)
        else:
            # print('w111111111111111111111',self.object)
            data['familymembers'] = FamilyMemberFormSet(instance=self.object)
            
            form_set = data['familymembers']
            for i, f in enumerate(form_set.forms, 0):
                try:
                    amount = data['familymembers'].queryset[i].TranAmount
                    if amount > 0:
                        f.initial['debit'] = amount
                        f.initial['credit'] = None
                    else:
                        f.initial['credit'] =-1* amount
                        f.initial['debit'] = None
                except:
                    f.initial['credit'] = None
                    f.initial['debit'] = None
        amount=0
        return data
    @transaction.atomic
    def form_valid(self, form):
        try:
            context = self.get_context_data()
            familymembers = context['familymembers']
        
            with transaction.atomic():
                self.object = None
              
                if familymembers.is_valid():
                    Totaldebit=0.00
                    TotalCredit=0.00
                    TotalCr=0.00
                    Totalde=0.00
                    i=0
                    for s in familymembers.forms:
                        
                        if (s.cleaned_data.get('debit')) and not(s.cleaned_data.get('DELETE', False)):
                            
                            Totalde   =  s.cleaned_data.get('debit')
                        if (s.cleaned_data.get('credit')) and not(s.cleaned_data.get('DELETE', False)):
                            TotalCr   =  s.cleaned_data.get('credit')
                         

                        Totaldebit    = Totaldebit + float(Totalde)
                        TotalCredit    = TotalCredit + float(TotalCr)
                        TotalCr=0.00
                        Totalde=0.00
                    if not (Totaldebit == TotalCredit) or (Totaldebit + TotalCredit)==0:
                        
                            messages.add_message(self.request, messages.INFO, "القيد غير متزن او  قم بادخال تفاصيل القيد")
                            return self.form_invalid(form)
                            # raise forms.ValidationError({"credit": "raise an error"})

                            # raise ValidationError("القيد غير متزن او  قم بادخال تفاصيل القيد")
                            #clear are u there
                            
                        # this raise ValidationError i wnat to send it to view 2 apply autocompleate on
                        # print('depbit 2 is {} crdeit2 is {}'.format(Totaldebit,TotalCredit))
                        # ValidationError("القيد غير متزن")  
                        # form.add_error(None, 'error description')
                        # messages.info( self , 'تأكد من  اسم المستخدم وكلمة المرور ')
                      
                         
                        # raise ValidationError("القيد غير متزن")  
                    
                    # print('total is =====',total)
                    # dir(ProfileFamilyMemberUpdate)
                    # result = familymembers.forset.aggregate(sum_of_ab=Sum("debit"))

                    # print ('result1168-------------------',  familymembers.forms.count() ) 
                    # print ('result21679-------------DELETE': True------', familymembers.cleaned_data.count() ) 
            
                    
                    for f in familymembers.forms:
                       
                                            
                        # print('f.cleaned_data', dir(f))  
                            
                        amount=0.00
                        # print(dir(f))
                        # print('- ---len--- 1---------------------------dir')
                        # print(f.cleaned_data.get('debit'))
                        # print('len(f.cleaned_data)issa is',len(f.cleaned_data))
                        
                      
                        # if  f.cleaned_data.get('DELETE', True):
                           
                        debit = f.cleaned_data.get('debit') # this come from form 
                        credit = f.cleaned_data.get('credit')
                       
                        # print('debit is {} credit {}'.format(debit,credit))   
                        if credit and debit:
                            messages.add_message(self.request, messages.INFO, "!!فضلا ادخل فقط الجانب الدائن او المدين في السطر الواحد")
                            return self.form_invalid(form)
                            #  self.form_invalid(form)
                             #raise ValidationError("!!فضلا ادخل فقط الجانب الدائن او المدين في السطر الواحد")
                        
                             
                        
                        elif  len(f.cleaned_data)==0:
                            continue
                     
                        elif len(f.cleaned_data)>0 and    (credit ==''   and debit ==''  ):
                            messages.add_message(self.request, messages.INFO, "!!لابد من ادخال الجانب الدائن او المدين")
                            return self.form_invalid(form)
                            # raise ValidationError("!!لابد من ادخال الجانب الدائن او المدين",not(credit  and debit  ))
                        
                        # return self.form_invalid(form) 
                        elif debit:
                            amount = float(debit)
                            debit=None
                        elif credit:
                            amount = -1 * float(credit)
                            credit=None
                        elif (debit is None) and (credit is None) and not (f.cleaned_data.get('DELETE', False) ):
                            messages.add_message(self.request, messages.INFO, "ادخل الجانب الدائن اوالمدين على الاقل")
                            return self.form_invalid(form)
                            
                            #   raise ValidationError("ادخل الجانب الدائن اوالمدين على الاقل")
                            #  return self.form_invalid(form) 
                                 
                        f.instance.TranAmount = amount
                    self.object            =None
                    self.object            = form.save(commit=False)
 
                    
                    # Cat=  self.request.GET.get('cat')
                    self.object.added_by    = self.request.user
                    
                    
                    familymembers.instance =  self.object
                    self.object.save()
                    count= familymembers.save()
                    
                    
                    if len(count) <2:
                        transaction.set_rollback(True)
                        messages.add_message(self.request, messages.INFO, "اعد ادخال القيد حدث خطأ اثناء حفظ القيد")
                        return self.form_invalid(form)

                    # self.object = form.save()
                    # # familymembers.instance = self.object
                    # familymembers.save()
                else:
                    transaction.set_rollback(True)
                    messages.add_message(self.request, messages.INFO,  familymembers.errors)
                    return self.form_invalid(form) 
                    # raise ValidationError(familymembers.errors )
                    # return render(request, 'template.html', {'form': form})
                    # return super(ProfileFamilyMemberUpdate, self).form_valid(familymembers.errors)
                # if familymembers.is_valid(): # is it FamilyMemberForm form?
                #     # print(familymembers.cleaned_data)
                #     familymembers.instance = self.object
                #     familymembers.save()
        except IntegrityError as e:
            transaction.set_rollback(True)
            messages.add_message(self.request, messages.INFO,e)
            return self.form_invalid(form)
             

        return super(ProfileFamilyMemberUpdate, self).form_valid(form)

    def form_invalid(self, form):
      
        # Whatever you wanna do. This example simply reloads the list
        self.object_list = self.get_queryset()
        context = self.get_context_data(task_form=form)
        return self.render_to_response(context)

class ProfileDelete(DeleteView):
    template_name ='Finance/transactionmaster_confirm_delete.html'
    model = TranTableMain
    success_url = reverse_lazy('profile-list')
 
def CurrencyCreate(request):
    form=CurrencyForm()
    if request.method=='POST':
        userid=request.user
        form= CurrencyForm(request.POST)
        if form.is_valid():
         
             fs= form.save(commit=False)
             fs.added_by= request.user
             fs.save()
    

             return redirect('Currency') 
    context={'form':form}
    return render(request, 'Finance/Currency_create.html', context )

def  Currency_edit(request,pk):
     #request.user.id
    items =  tbcurrency.objects.get(id=pk)
    form = CurrencyFormUpdate(instance=items)
    if request.method == 'POST':
         form = CurrencyFormUpdate(request.POST, instance=items)
         
         if form.is_valid():
            fs= form.save(commit=False)
            fs.added_by= request.user
            fs.save()
            return redirect('Currency')

    context={'form':form}
    return render(request, 'Finance/Currency_create.html', context )
 
def Currency_delete(request,pk):
    item = tbcurrency.objects.get(id=pk)
    if request.method == "POST":
	    item.delete()
	    return redirect('Currency')

    context = {'item':item}
    return render(request, 'Finance/delete.html', context)
     

def Currency(request):

    item_list = tbcurrency.objects.all().order_by('id') 
    myFilter = CurrencyFilter(request.GET, queryset=item_list)
    form = myFilter.qs 

    page = request.GET.get('page', 1)

    paginator = Paginator(form, 7)
    try:
        form = paginator.page(page)
    except PageNotAnInteger:
         form = paginator.page(1)
    except EmptyPage:
         form = paginator.page(paginator.num_pages)
    context={'form': form ,'myFilter':myFilter}
    return render(request, 'Finance/Currency.html',context)

#Costcenter
def CostCenterCreate(request):
    form=CostCenterForm()
    if request.method=='POST':
        form= CostCenterForm(request.POST)
        if form.is_valid():
            print(request.user)
            fs= form.save(commit=False)
            fs.added_by= request.user
            fs.save()
            return redirect('costcenter') 
    context={'form':form}
    return render(request, 'Finance/costcenter_create.html', context)

def  costcentere_edit(request,pk):
    
    order = costcenter.objects.get(id=pk)
    form = CostCenterFormUpdate(instance=order)
    if request.method == 'POST':
        form = CostCenterFormUpdate(request.POST, instance=order)
         
        if form.is_valid():
            fs= form.save(commit=False)
            fs.added_by= request.user
            fs.save()
            return redirect('costcenter')
        else:
            raise form.ValidationError( 'تاكد من ادخال البياناتالمطلوبة بصورة صحيحة')
          # messages.info(request, 'تاكد من ادخال البياناتالمطلوبة بصورة صحيحة')
    context={'form':form}
    return render(request, 'Finance/costcenter_create.html', context )
 
def costcentere_delete(request,pk):
    
    ccenter = costcenter.objects.get(id=pk)
    if request.method == "POST":
	    ccenter.delete()
	    return redirect('costcenter')

    context = {'item':ccenter}
    return render(request, 'Finance/delete-costcenter.html', context)

def Costcenter(request):

    Costcenter_list = costcenter.objects.all().order_by('id') 
    myFilter = CostCFilter(request.GET, queryset=Costcenter_list)
    Costcenter = myFilter.qs 

    page = request.GET.get('page', 1)

    paginator = Paginator(Costcenter, 7)
    try:
        Costcenter = paginator.page(page)
    except PageNotAnInteger:
        Costcenter = paginator.page(1)
    except EmptyPage:
        Costcenter = paginator.page(paginator.num_pages)

 
    context={'Costcenter': Costcenter ,'myFilter':myFilter}
    return render(request, 'Finance/costcenter.html',context)