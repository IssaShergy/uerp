from django.urls import path
 
from . import views
 
from django.conf.urls import url
#from idlelib import autocomplete
 
from Finance.models import Account
from .views import  default_map,mark_your_attendance,mark_your_attendance_out,index
from SecurityGuard.views import listall
 

urlpatterns = [
    
     
    # url(r'', views.default_map, name="default"),
    path('SecurityGuard', views.index ,name='SecurityGuard'),
    path('mark-your-attendance-out', views.mark_your_attendance_out, name='mark-your-attendance-out'),
    path('listall',  views.listall ,name='listall'),
    path('mark-your-attendance', views.mark_your_attendance, name='mark-your-attendance'),
#     path('GeneratePdf',  GeneratePdf.as_view(),name='GeneratePdf'),
#     path('profile-lis', views.ProfileList, name='profile-list'),
#     path('profile/add/', views.ProfileFamilyMemberCreate.as_view(),{'cat':'p'}, name='profile-add'),
#     path('profile/<int:pk>', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
#     path('profile-delete/<int:pk>', views.ProfileDelete.as_view(), name='profile-delete'),
#     #Currency  
#     # path('create_normal', views.create_book_normal, name='create_book_normal'),
#     path('Currency', views.Currency, name='Currency'),
#     path('Currency_create', views.CurrencyCreate, name='Currency_create'),
#     path('currency_edit/<int:pk>/', views.Currency_edit, name="currency_edit"),
#     path('Currencydelete/<int:pk>/', views.Currency_delete, name="Currencydelete"),
    
#    # costcenter
#     # path('create_Receipt', views.create_book_normal, name='create_Receipt'),
#     path('costcenter', views.Costcenter, name='costcenter'),
#     path('costcenter_create', views.CostCenterCreate, name='costcenter_create'),
#     path('costcentere_edit/<int:pk>/', views.costcentere_edit, name="costcentere_edit"),
#     path('costcentere_delete/<int:pk>/', views.costcentere_delete, name="costcentere_delete"),
]