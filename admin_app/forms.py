from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from Finance.models import costcenter
 
 
 

class CompanyForm(ModelForm):
	def __init__(self, *args, **kwargs):
			super(ModelForm, self).__init__(*args, **kwargs)
			self.fields['name'].label = 'اسم الشركة'	
			self.fields['mobile'].label = 'جوال '
			self.fields['phone'].label = 'هاتف' 
			self.fields['taxNumber'].label = 'الرقم الضريبي'
			self.fields['company_pic'].label = 'الشعار'
	class Meta:
		model = Company
		fields = '__all__'

class branchForm(ModelForm):
	def __init__(self, *args, **kwargs):
			super(ModelForm, self).__init__(*args, **kwargs)
			self.fields['name'].label = 'اسم الفرع'	
			self.fields['mobile'].label = 'جوال '
			self.fields['phone'].label = 'هاتف' 
			self.fields['address'].label = 'هاتف'
			self.fields['company'].label = 'هاتف'
			self.fields['branch_pic'].label = 'الشعار'
	class Meta:
		model = branch
		fields = '__all__'

		#exclude = ['user']


class branchFormUpdate(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'اسم الفرع'
		self.fields['name'].label = 'اسم الفرع'	
		self.fields['mobile'].label = 'جوال '
		self.fields['phone'].label = 'هاتف' 
		self.fields['address'].label = 'هاتف'
		self.fields['company'].label = 'هاتف'
		self.fields['branch_pic'].label = 'الشعار'
	class Meta:
            model=branch
            fields= '__all__'     #['id','name']

	def clean_name(self):
       
		cd = self.cleaned_data
       
     
		if cd['name'] =='':
			raise forms.ValidationError(' فضلا ادخل اسم الفرع  .')
			return cd['name']
        
		name = self.cleaned_data['name']
		if branch.objects.exclude(pk=self.instance.pk).filter(name=name).exists():
			raise forms.ValidationError('الاسم "%s" مستخدم مسبقاً.' % name)
		return name

# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'


class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='اختياري.')
	last_name = forms.CharField(max_length=30, required=False, help_text='اختياري.')
	Ccenter = forms.ModelChoiceField(
             queryset=costcenter.objects.all(),
            label=u"مركز التكلفة", required= False,
            
        )
	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email', 'password1', 'password2','Ccenter']
		#labels = {'username': "Student Number",}
		help_texts = {'username': "ادخل اسم المستخدم",'email': "",'password1': "password1",'password2': "" }
	def __init__(self, *args, **kwargs):
			super(ModelForm, self).__init__(*args, **kwargs)
			self.fields['username'].label = 'اسم المستخدم'	
			self.fields['email'].label = 'البريد الاليكتروني '
			self.fields['password1'].label = 'كلمة المرور' 
			self.fields['password2'].label = 'اعادة ادخال كلمة المرور'
			self.fields['first_name'].label = 'الاسم الاول'
			self.fields['last_name'].label = 'الاسم الثاني'
			

