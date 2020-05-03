import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
from django import forms
from distutils.util import strtobool
 
BOOLEAN_CHOICES = (('', 'الكل'),('False', 'غير مرحل'), ('True', 'مرحل'),)

class TranMainFilter(django_filters.FilterSet):
    	TranNo = CharFilter(label='بحث برقم القيد',field_name='TranNo', lookup_expr='icontains')
    	Post = django_filters.TypedChoiceFilter(label='الحالة',field_name='Post',choices=BOOLEAN_CHOICES,
                                            coerce=strtobool)

    	start_date = DateFilter(label='من تاريخ',field_name="TranDate", lookup_expr='gte')
    	end_date   = DateFilter(label='الى',field_name="TranDate", lookup_expr='lte')
    	class Meta:
    			model= TranTableMain
    			fields=['TranNo', ]

class CostCFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	# end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	name = CharFilter(label='  بحث باسم المركز  ',field_name='name', lookup_expr='icontains')
	id = CharFilter(label='  بحث بكود المركز  ',field_name='id', lookup_expr='icontains')
	 
	class Meta:
		model = costcenter
		fields = '__all__'
		#exclude = ['customer', 'date_created']

class CurrencyFilter(django_filters.FilterSet):
		name = CharFilter(label='  بحث باسم العملة  ',field_name='name', lookup_expr='icontains')
		symbol = CharFilter(label='بحث برمز العملة',field_name='id', lookup_expr='icontains')
		class Meta:
    			model= tbcurrency
    			fields=['name', 'symbol'] #'__all__'
	
	# class Meta:
	# 	model = costcenter
	# 	#fields = '__all__'
	# 	exclude = ['name', 'symbol']