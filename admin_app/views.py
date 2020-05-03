from django.shortcuts import render,redirect
from .models import *
from .forms import  CompanyForm,branchForm,branchFormUpdate,CreateUserForm
from .filters import  branchFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import auth
from  .decorators  import unauthenticated_user, allowed_users, admin_only

# @login_required(login_url='login')
# @admin_only
def index(request):
    return render(request, 'admin_app/dashboard.html')

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def branch_delete(request,pk):
    
    item = branch.objects.get(id=pk)
    if request.method == "POST":
	    item.delete()
	    return redirect('branch_show')

    context = {'item':item}
    return render(request, 'admin_app/delete.html', context)
    
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def  branch_edit(request,pk):
       
    order = branch.objects.get(id=pk)
    form = branchFormUpdate(instance=order)
    if request.method == 'POST':
        form = branchFormUpdate(request.POST,request.FILES, instance=order)
         
        if form.is_valid():
            form.save()
            return redirect('branch_show')

    context={'form':form,'branchs':order}
    return render(request, 'admin_app/branch_create.html', context )

def logoutUser(request):
    print('logout issa:',request.user.id)
    logout(request)
    return redirect('login')

def branchCreate(request):
    form=branchForm()
    if request.method=='POST':
        form= branchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_show') 
    context={'form':form}
    return render(request, 'admin_app/branch_create.html', context )

def CompanySettings(request):
   
    company = Company.objects.first()
    form = CompanyForm(instance=company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES,instance=company)
        if form.is_valid():
            form.save()
    context = {'form':form,'company':company}
    return render(request, 'admin_app/Compny_settings.html', context)

def BranchFn(request):
    branch_list = branch.objects.all().order_by('id') 
    myFilter = branchFilter(request.GET, queryset=branch_list)
    branchs = myFilter.qs 

    page = request.GET.get('page', 1)

    paginator = Paginator(branchs, 7)
    try:
        branchs = paginator.page(page)
    except PageNotAnInteger:
        branchs = paginator.page(1)
    except EmptyPage:
        branchs = paginator.page(paginator.num_pages)

 
    context={'Costcenter': branchs ,'myFilter':myFilter}
    return render(request, 'admin_app/branch.html',context)

def tables(request):
    return render(request, 'admin_app/tables.html')

 
def morris(request):
    return render(request, 'admin_app/morris.html')

def forms(request):
    return render(request, 'admin_app/forms.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'تأكد من  اسم المستخدم وكلمة المرور ')

    context = {}
    return render(request, 'admin_app/login.html', context)
# @login_required(login_url='login')
# @admin_only
def registerPage(request):
    
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
        
			username = form.cleaned_data.get('username')

			# group = Group.objects.get(name='customer')
			# user.groups.add(group)
			#Added username after video because of error returning customer name if not added
			# Customer.objects.create(
			# 	user=user,
			# 	name=user.username,
			# 	)

			messages.success(request, 'تم انشاء مستخدم بنجاح' + 'username')
              
			return redirect('register')
		

	context = {'form':form}
	return render(request, 'admin_app/register.html', context)

def panels_wells(request):
    return render(request, 'admin_app/panels_wells.html')

def buttons(request):
    return render(request, 'admin_app/buttons.html')

def notifications(request):
    return render(request, 'admin_app/notifications.html')

def typography(request):
    return render(request, 'admin_app/typography.html')

def icons(request):
    return render(request, 'admin_app/icons.html') 

def grid(request):
    return render(request, 'admin_app/grid.html')   
 