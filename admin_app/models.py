from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
  # payment_date = fields.Date(string='Payment Date', default=fields.Date.context_today, required=True, copy=False)
class Company(models.Model):
        #user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
        name=models.CharField(unique=True, max_length=100,null=False ,blank= True)
        phone=models.CharField(max_length=20,null=False ,blank= True)
        mobile=models.CharField(max_length=20,null=False ,blank= True)
        taxNumber=models.CharField(max_length=20,null=False ,blank= True)
        company_pic=models.ImageField(default="profile1.png",null=True,blank=True)   
        def __str__(self):
            return self.name
class branch(models.Model):
        #user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
        company = models.ForeignKey(Company, null=False, on_delete= models.CASCADE)
        name=models.CharField(unique=True, max_length=100,null=False ,blank= True)
        phone=models.CharField(max_length=20,null=False ,blank= True)
        mobile=models.CharField(max_length=20,null=False ,blank= True)
        address=models.CharField(  max_length=200,null=True ,blank= True)
        branch_pic=models.ImageField(default="profile1.png",null=True,blank=True)   
        def __str__(self):
            return self.name
 

