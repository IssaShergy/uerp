from django.db import models
from django.template import Library
from datetime import datetime  
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from admin_app.models import branch
from django.urls import reverse
from django.utils import timezone 
from django.db.models import Count,Max,Min,Sum
from six import python_2_unicode_compatible
from django.db.models import ProtectedError
from django.utils.translation import ugettext_lazy
from django.core.validators import MinValueValidator, MaxValueValidator

class Town(models.Model):
    name = models.CharField(max_length=50)
    county = models.CharField(max_length=50)

    class Meta:
        ordering = ['county', 'name']

    def __unicode__(self):
        return self.name


class Weather(models.Model):
    town = models.ForeignKey(
        Town,
        related_name=ugettext_lazy('town'),on_delete=models.PROTECT)
    date = models.DateField()
    description = models.TextField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    wind_speed = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name=ugettext_lazy('wind speed'))
    precipitation = models.IntegerField(
        verbose_name=ugettext_lazy('precipitation'))
    precipitation_probability = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=ugettext_lazy('precipitation probability'))
    observations = models.TextField(
        verbose_name=ugettext_lazy('weather observations'))

    class Meta:
        verbose_name_plural = ugettext_lazy('weather')
        unique_together = (('town', 'date'))
        ordering = ['-date', 'town']

    def __unicode__(self):
        dtos = self.date.strftime('%d-%m-%Y')
        return self.town.name + " " + dtos


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name
        
#ModelName.objects.aggregate(Sum('field_name'))
#  django_currentuser.db.models 
 #chart of 
#  cc_myself = forms.BooleanField(required=False)
# name = forms.TextInput(attrs={'required': True})
#  day = forms.DateField(initial=datetime.date.today)
#  >>> formset.errors
# [{}, {'pub_date': ['This field is required.']}]
# >>> len(formset.errors)
# 2
# >>> formset.total_error_count()
# ArticleFormSet = formset_factory(ArticleForm, min_num=3, validate_min=True)
# -----------------
# for form in formset.ordered_forms:
#     ...     print(form.cleaned_data)
# -------------------------------------
# from django import forms

# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(
#         max_length=3,
#         widget=forms.Select(choices=TITLE_CHOICES),
#     )
#     birth_date = forms.DateField(required=False)

# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
#     =========================================================
# save_m2m
# =======================================
# from django.forms import ModelForm, Textarea
# from myapp.models import Author

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         widgets = {
#             'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#         }
# ====================ok=====================
# >>> from django.forms import Textarea
# >>> Form = modelform_factory(Book, form=BookForm,
# ...                          widgets={"title": Textarea()})
# ---------for what main account ? its main check box ok-------------------------------
 
class Account(models.Model):
        pId = models.IntegerField(default=None, blank=True, null=True)
        name = models.CharField(max_length=100)
        accountcode = models.IntegerField(default=0,null=False)
        mainaccount = models.IntegerField(default=0)
        def __str__(self):
             return self.name

        def delete_r(self):
            children = Account.objects.filter(pId=self.id)
            for account in children:
                account.delete_r()
            self.delete()

def currency_display(amount):
    return '{:0.2f}'.format(amount) if amount else '0.00'


class yearTBL(models.Model):
    CurentYear  = models.IntegerField(null=False,blank=False)
    oldYear     = models.IntegerField( null=False,blank=False)
    branchName  = models.ForeignKey(branch,on_delete=models.PROTECT,null=False,blank=False)
    trannoclose =models.IntegerField(  null=False,blank=False)
    trannoopen  =models.IntegerField(null=False,blank=False)
    status      =models.BooleanField(default=False,null=False)
  
    def __Unicode__(self):
        return self.CurentYear

class tbcurrency(models.Model):
 
    created       =models.DateTimeField(auto_now_add=True)   
    updated       =models.DateTimeField(auto_now=True)
    name          =models.CharField( unique= False,default='-' ,max_length=100,null=False ,blank= True  ) #help_text=_('قم بادخال اسم  العملة  ')
    Singlname     =models.CharField(max_length=10,null=True ,blank= True  )#help_text=_('اسم العملة المفرد'),
    collectionname=models.CharField(max_length=20,null=True ,blank= True  )#help_text=_('اسم العملة الجمع'),
    partname      =models.CharField(max_length=10,null=True ,blank= True  )#help_text=_(' اسم جزء العملة'),
    Sympol        =models.CharField(max_length=10,null=True ,blank= True  )#help_text=_('الرمز '),
    Cpartname     =models.CharField(max_length=15,null=True ,blank= True  )#help_text=_('اسم جزء العملة جمع'),
    rate          =models.DecimalField(max_digits=5, decimal_places=2,default=1)#help_text=_('المعدل'),
    equivalent    =models.DecimalField(max_digits=5, decimal_places=2,default=0)#help_text=_('المكافئ'),
    added_by      = models.ForeignKey(User,null=False, blank=True, on_delete=models.PROTECT)
    def __str__(self):
            return self.name


class costcenter(models.Model):
    
    added_by      = models.ForeignKey(User,null=False, blank=True, on_delete=models.PROTECT)
    
    name          =models.CharField("اسم المركز",unique=True,help_text=_('قم بادخال اسم المركز المالي  '),max_length=100,null=False ,blank= True)
 
    
    def __str__(self):
            return self.name
 
# def _GetTranNO():
#         check=False
#         if check:
#             trnno = "{0}".format(2020)
#         else:
#             tran_max=TranTableMain.objects.aggregate(Tran_max=Max('TranNo'))
#         return trnno
# conected with tran master slave 
class TranTableMain(models.Model): # this master table
    # try:

        notebookNum    = models.IntegerField('الرقم الدفتري',null=True,blank=True)
        description    = models.CharField("ملحوظة", max_length=200,null=True,blank=True)
        checkdate      = models.DateTimeField("تاريخ الشيك",  null=True, default=datetime.now)
        updated        = models.DateTimeField(auto_now=True)
        #created        = models.DateTimeField(auto_now_add=True ,default=datetime.now )     
        TranNo         = models.BigIntegerField("رقم القيد",null=   False,unique=True )
        TranDate       = models.DateTimeField("التاريخ" , auto_now=False, auto_now_add=False)
        Post           = models.BooleanField("الترحيل",default=False,null=False)
        Cate           = models.CharField(null= False,blank=True ,max_length=2)    
        added_by       = models.ForeignKey(User,null=False, blank=True, on_delete=models.PROTECT)
        branchName     = models.ForeignKey(branch,on_delete=models.PROTECT,null=False,blank=False)   
        serial         = models.IntegerField("رقم السند",null=True)
        yeartran       = models.ForeignKey(yearTBL,null=True, blank=True, on_delete=models.PROTECT)
        
        
        def save(self,*args,**kwargs):
               
            
               
                currentyear     =  yearTBL.objects.first()
                self.yeartran   =  currentyear
                # self.added_by   = User.objects.get(id=1) ;
              
                super(TranTableMain,self).save(*args,**kwargs)

    #  def __unicode__(self):
    #         return '{0}/{1} - {2}'.format(self.date.year, self.date.month,
    #                                   self.name)
    # full_number = "{0}-{1:02d}000".format(self.type,
    #                                               self.account_number())
            
        # def __str__(self):
        #  return self.description

    # except ProtectedError :    
    #     print('error is ====================')
    # python manage.py makemigrations --name hh1 Finance
 
#this table   TranAmount we need to save   save depit or credit here TranAmount 
class TranTable(models.Model):  # this sleave fk tranTableMain
    AccountCode= models.ForeignKey(Account,on_delete=models.PROTECT,null=False,blank=False)
    jurnaldesc     = models.CharField("البيان", max_length=200,null=False,blank=False)
    TranAmount     = models.FloatField("المبلغ",null=True, blank=True)
    updated        = models.DateTimeField(auto_now=True )
   # created        = models.DateTimeField(auto_now_add=True,default=timezone.now()  ) 
    TranNo         = models.BigIntegerField("رقم القيد",default=0 )
    Ccenter        = models.ForeignKey(costcenter,on_delete=models.PROTECT,null=True,blank= True)
    # added_by       = models.ForeignKey(User,null= True, blank=True, on_delete=models.PROTECT)
    tranTableMain  = models.ForeignKey(TranTableMain,null=False, blank=True, on_delete=models.CASCADE)
    # def save(self,*args,**kwargs):
    #         self.Cate ='c' ;
            
          
    #         super(TranTable,self).save(*args,**kwargs) 
    # def __str__(self):
    #     return self.jurnaldesc if self.jurnaldesc else "empty"
    # are you there
    # def debit(self):
    #         return currency_display(-self.TranAmount) if self.TranAmount < 0 else ''
    # def credit(self):
    #       return currency_display(self.TranAmount) if self.TranAmount > 0 else ''

   
#    @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()