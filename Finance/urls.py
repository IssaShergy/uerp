from django.urls import path
 
from . import views
 
from django.conf.urls import url
#from idlelib import autocomplete
from dal import autocomplete
from Finance.models import Account
from Finance.views import GeneratePdf, invoice_view,Geo
 

urlpatterns = [
    
     
    url(r'^ajax/validate_username/$', views.Post_, name='validate_username'),
    # url(
    #     r'^country-autocomplete/$',
    #     CountryAutocomplete.as_view(),
    #     name='country-autocomplete',
    # ),
    # url(
    #     'test-autocomplete/$',
    #     autocomplete.Select2QuerySetView.as_view(model=Account),
    #     name='select2_fk',
    # ),
    # path('country-autocomplete', CountryAutocomplete.as_view(), name='country-autocomplete'),
    # path('list', views.list, name='list'),
       
    #Chart of account
    path('Geo', views.Geo,name='Geo'),
    path('chartofaccount', views.index,name='chartofaccount'),
    path('get', views.get),
    path('create', views.create),
    path('update', views.update),
    path('delete', views.delete),
    path('invoice',views.invoice_view,name='invoice'),

    path('GeneratePdf',  GeneratePdf.as_view(),name='GeneratePdf'),
    path('profile-lis', views.ProfileList, name='profile-list'),
    path('profile/add/', views.ProfileFamilyMemberCreate.as_view(),{'cat':'p'}, name='profile-add'),
    path('profile/<int:pk>', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
    path('profile-delete/<int:pk>', views.ProfileDelete.as_view(), name='profile-delete'),
    #Currency  
    # path('create_normal', views.create_book_normal, name='create_book_normal'),
    path('Currency', views.Currency, name='Currency'),
    path('Currency_create', views.CurrencyCreate, name='Currency_create'),
    path('currency_edit/<int:pk>/', views.Currency_edit, name="currency_edit"),
    path('Currencydelete/<int:pk>/', views.Currency_delete, name="Currencydelete"),
    
   # costcenter
    # path('create_Receipt', views.create_book_normal, name='create_Receipt'),
    path('costcenter', views.Costcenter, name='costcenter'),
    path('costcenter_create', views.CostCenterCreate, name='costcenter_create'),
    path('costcentere_edit/<int:pk>/', views.costcentere_edit, name="costcentere_edit"),
    path('costcentere_delete/<int:pk>/', views.costcentere_delete, name="costcentere_delete"),
]