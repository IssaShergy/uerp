from django.urls import path
from django.conf.urls import url
from . import views
 
# from django.contrib.admin.views import autocomplete
#app_name = 'admin_app'
from dal import autocomplete
from Finance.models import Account
urlpatterns = [
      

    #  url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # path('costcenter', views.Costcenter, name='costcenter'),
    # path('costcenter_create', views.CostCenterCreate, name='costcenter_create'),
    # path('costcentere_edit/<int:pk>/', views.costcentere_edit, name="costcentere_edit"),
    # path('costcentere_delete/<int:pk>/', views.costcentere_delete, name="costcentere_delete"),
]