from django.forms import ModelForm
from .models import costcenter,tbcurrency,Account ,TranTableMain,TranTable
from django import forms
from django.forms import formset_factory
from django.forms import ModelForm, inlineformset_factory
from decimal import Decimal
from dal import autocomplete 
from django.db.models import ProtectedError
from django.forms import BaseFormSet
from django.core.validators import RegexValidator
from Finance.models import Customer
from .models import Weather, Town

 
class WeatherForm(forms.ModelForm):
    town = forms.ModelChoiceField(
        queryset=Town.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Weather
        fields = ['town']


# Receipt السندات
class InvoiceForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
        ('html', 'HTML'),
    )
    number = forms.CharField(label='Invoice #')
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    subject = forms.CharField()
    amount = forms.DecimalField()
    format = forms.ChoiceField(choices=FORMAT_CHOICES)

class ProfileForm(ModelForm):
    class Meta:
        model = TranTableMain
        exclude = ()
        appointment_date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', )
        )


        # def clean(self):  
        #  for form in self.forms:
        #         if self.can_delete and self._should_delete_form(form):
        #             continue
        #         notebookNum = form.cleaned_data.get('notebookNum')
        #         print('jurnaldesc1=================',notebookNum)  

class FamilyMemberForm(ModelForm):
    AccountCode = forms.ModelChoiceField(
            queryset=Account.objects.filter(mainaccount=False),
            label=u"اسم الحساب",
            
        )

    Ccenter = forms.ModelChoiceField(
             queryset=costcenter.objects.all(),
            label=u"مركز التكلفة", required= False,
            
        )

    debit = forms.FloatField( label='مدين', required=False, widget=forms.TextInput(
           
            attrs={  'style':'width:90px ;border: .0px  ', 'class': 'form-control debit'}))
    credit = forms.FloatField( label='دائن', required=False, widget=forms.TextInput(
           attrs={  'style':'width:90px ;border: .0px solid', 'class': 'form-control credit'}))
    jurnaldesc = forms.CharField(label='ملاحظات',  required=True, widget=forms.TextInput(
           attrs={  'style':'border: .0px solid', 'class': 'form-control  testclass'}))
    
    
    # city = forms.ModelChoiceField(
    #     queryset=Account.objects.filter(mainaccount=True),
    #     label=u"issa",
         
    # )


    class Meta:
        model = TranTable # both are different TranTableMain both us in inline formset factor
        fields= ('AccountCode','Ccenter','debit','credit','jurnaldesc',  )
         

        # exclude = ()
        # def clean_(self):
        #     cleaned_data = super().clean()
        #     cd = self.cleaned_data
        #     if cd['jurnaldesc'] =='':
        #         raise forms.ValidationError(' فضلا ادخل  رقم الدفتري    .')
        #         return cd['jurnaldesc']
           
       


         
        # def __init__(self, *args, **kwargs):
        #     super(FamilyMemberForm, self).__init__(*args, **kwargs)

        # def clean_jurnaldesc(self):
        #     jurnaldesc = self.cleaned_data['jurnaldesc']
        #     print('jurnal ------------is----- {}'.format(jurnaldesc))
        #     return  jurnaldesc 
            
        # check  data came from form but not work 
        # def clean(self):
        #     # it's not coming here what is slution 
        #     # wait
        #     """
        #     Make sure only a credit or debit is entered and set it to the
        #     balance_delta.
          
        #     """
          
        #     super(FamilyMemberForm, self).clean()
           
        #     print(self.cleaned_data)

        #     if any(self.errors) or self.cleaned_data.get('DELETE', False):
        #         # return self.cleaned_data
        #         cleaned_data = self.cleaned_data
        #         print(cleaned_data)
        #         debit = cleaned_data.get('debit') # this come from form 
        #         credit = cleaned_data.get('credit')# this come from form  can you work debg line by line
        #         print(debit, credit)
        #         print(type(debit), type(credit))
        #     if credit and debit:
        #         raise forms.ValidationError("Please enter only one debit or "
        #                                     "credit per line.")
        #     elif credit:
        # overite like this        cleaned_data['TranAmount'] = -1 * float(credit)
        #     elif debit:
        #         cleaned_data['TranAmount'] = float(debit)
        #     else:
        #         raise forms.ValidationError("Either a credit or a debit is "
        #                                     "required")
        #     print('clean data is ----------{}'.format(cleaned_data['TranAmount']))
        #     return cleaned_data  #   cleaned_data['TranAmount']  amount val credit and debit not present in table 

        # widgets = {
        #     'AccountCode': autocomplete.ModelSelect2(url='test-autocomplete/')
        # }
        # widgets = {
        #     'accountcode': autocomplete.ModelSelect2(url='country-autocomplete')
        # }
        # widgets = {
        #     'AccountCode': autocomplete.ModelSelect2(url='country-autocomplete')
        # }
        # widgets = {
            
        #     # 'AccountCode': autocomplete.ModelSelect2(url='country-autocomplete'),
                                
        #     'jurnaldesc': forms.TextInput(
        #         attrs={'class': 'form-control enter-mod'}),
            
        #     'AccountCode': forms.Select(
        #         attrs={'class': 'form-control enter-mod'}),
        # }
        # widgets = {'accountcode': autocomplete.ModelSelect2(url='select2_fk')}
        
        
        # def clean(self):
        #     """
        # Make sure only a credit or debit is entered and set it to the
        # balance_delta.

        # """
            # super(FamilyMemberForm, self).clean()
            # if any(self.errors) or self.cleaned_data.get('DELETE', False):
            #     return self.cleaned_data
            # cleaned_data = self.cleaned_data
            # debit = cleaned_data.get('debit')
            # credit = cleaned_data.get('credit')
            # if credit and debit:
            #     raise forms.ValidationError("Please enter only one debit or "
            #                                 "credit per line.")
            # elif credit:
            #     cleaned_data['TranAmount'] = credit
            # elif debit:
            #     cleaned_data['TranAmount'] = -1 * debit
            # else:
            #     raise forms.ValidationError("Either a credit or a debit is "
            #                                 "required")
            # return cleaned_data

FamilyMemberFormSet = inlineformset_factory(TranTableMain, TranTable,
                                            form=FamilyMemberForm, extra=1)

# Profile.objects.all().aggregate(Max('id'))['id__max']

# for p in Profile.objects.raw('SELECT Max(id) FROM myprofile_rofile'):
#     ...     print(p)


# class TranTableForm(ModelForm):

    # jurnaldesc = forms.CharField(label='2البيان', required=False, widget=forms.TextInput(
    #        attrs={  'style':'width:60px ;border: .0px solid;opacity: .5;', 'class': 'name'}))
    # TranAmount = forms.CharField(label='المبلغ', required=False, widget=forms.TextInput(
    #        attrs={   'maxlength': 10, 'style':'width:60px ;border: .0px solid;opacity: .5;', 'class': 'testclass'}))
#     class Meta:
#         model = TranTable
#         # fields='__all__'
#         exclude = ()
# TranTableFormSet = inlineformset_factory(TranTableMain, TranTable,form=TranTableForm, extra=1)

# class TranTableMainForm(forms.Form):
#     # description = forms.CharField(label='2البيان' ,required=False, widget=forms.TextInput(
#         #    attrs={  'style':'width:120px ;border: .0px solid;opacity: .5;', 'class': 'name'}))
#     # description = forms.CharField(label='البيان', required=False, widget=forms.TextInput(
#     #        attrs={  'style':'width:120px ;border: .0px solid;opacity: .5;', 'class': 'name'}))
     
#     class Meta:
#         model = TranTableMain
#         #fields ='__all__' #('added_by','description')
#         exclude = ()
         
#finance
class CostCenterForm(ModelForm):
    def __init__(self, *args, **kwargs):
              super(ModelForm, self).__init__(*args, **kwargs)
              self.fields['name'].label = 'مركز التكلفة'
       
    class Meta:
            model=costcenter
            fields= '__all__'     #['id','name']

    def clean_name(self):
        cleaned_data = super().clean()
        cd = self.cleaned_data
        
         
        if cd['name'] =='':
             raise forms.ValidationError(' فضلا ادخل اسم المركز  .')
             return cd['name']

        if costcenter.objects.filter(name=cd['name']).exists():
                    raise forms.ValidationError('!!!يوجد مركز  مسجل بهذا الاسم.')
        return cd['name']

class CostCenterFormUpdate(ModelForm):
    # def __init__(self, *args, **kwargs):
    #           super(ModelForm, self).__init__(*args, **kwargs)
    #           self.fields['name'].label = 'مركز التكلفة'
       
    class Meta:
            model=costcenter
            fields= '__all__'     #['id','name']

    def clean_(self):
       
        cd = self.cleaned_data
       
     
        if cd['name'] =='':
             raise forms.ValidationError(' فضلا ادخل اسم المركز  .')
             return cd['name']
        
        name = self.cleaned_data['name']
        if costcenter.objects.exclude(pk=self.instance.pk).filter(name=name).exists():
            raise forms.ValidationError('الاسم "%s" مستخدم مسبقاً.' % name)
        return name

class CurrencyForm(ModelForm):
    # symbol = forms.CharField(label='', required=False, widget=forms.TextInput(
    #      attrs={'style':'width:10em',"placeholder": "رمز العملة", 'class': 'form-control w-100'}))
    def __init__(self, *args, **kwargs):
               super(ModelForm, self).__init__(*args, **kwargs)
               self.fields['name'].label = 'اسم العملة'
               self.fields['Singlname'].label ='اسم العملة المفرد' 
               self.fields['collectionname'].label ='اسم العملة الجمع' 
 
               self.fields['Sympol'].label ='رمز العملة' 
               self.fields['partname'].label ='اسم جزء العملة' 
               self.fields['Cpartname'].label ='اسم جزء العملة جمع' 
               self.fields['rate'].label ='المعدل' 
               self.fields['equivalent'].label ='المكافئ' 
              

    class Meta:
            model=tbcurrency
            fields= '__all__'     #['id','name']

    def clean_name(self):
        cleaned_data = super().clean()
        cd = self.cleaned_data
        if cd['name'] =='':
             raise forms.ValidationError(' فضلا ادخل اسم العملة  .')
             return cd['name']

        if tbcurrency.objects.filter(name=cd['name']).exists():
                     raise forms.ValidationError('اسم العملة مستخدم.')
        return  cd['name']

class CurrencyFormUpdate(ModelForm):
     def __init__(self, *args, **kwargs):
               super(ModelForm, self).__init__(*args, **kwargs)
               self.fields['name'].label = 'اسم العملة'
               self.fields['Singlname'].label ='اسم العملة المفرد' 
               self.fields['collectionname'].label ='اسم العملة الجمع' 
 
               self.fields['Sympol'].label ='رمز العملة' 
               self.fields['partname'].label ='اسم جزء العملة' 
               self.fields['Cpartname'].label ='اسم جزء العملة جمع' 
               self.fields['rate'].label ='المعدل' 
               self.fields['equivalent'].label ='المكافئ' 
            
     class Meta:
             model= tbcurrency
             fields= '__all__'     #['id','name']

     def clean_name(self):
       
         cd = self.cleaned_data
       
     
         if cd['name'] =='':
              raise forms.ValidationError(' فضلا ادخل اسم العملة  .')
              return cd['name']
        
         name = self.cleaned_data['name']
         if tbcurrency.objects.exclude(pk=self.instance.pk).filter(name=name).exists():
             raise forms.ValidationError('الاسم "%s" مستخدم مسبقاً.' % name)
         return name
 
        
        
            