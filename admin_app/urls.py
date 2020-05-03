from django.urls import path

from . import views

#app_name = 'admin_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('tables', views.tables, name='tables'),
    path('morris', views.morris, name='morris'),
    path('register', views.registerPage, name='register'),
    path('forms', views.forms, name='forms'),
    path('panels_wells', views.panels_wells, name='panels_wells'),
    path('buttons', views.buttons, name='buttons'),
    path('notifications', views.notifications, name='notifications'),
    path('typography', views.typography, name='typography'),
    path('icons', views.icons, name='icons'),
    path('grid', views.grid, name='grid'),
    path('login', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('CompanySettings', views.CompanySettings, name='CompanySettings'),
    path('branch_show', views.BranchFn, name='branch_show'),
    path('branch_create', views.branchCreate, name='branch_create'),
    path('branch_edit/<int:pk>/', views.branch_edit, name="branch_edit"),
    
    path('branch_delete/<int:pk>/', views.branch_delete, name="branch_delete"),


 
]