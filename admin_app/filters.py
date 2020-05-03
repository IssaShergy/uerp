import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class branchFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	# end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	name = CharFilter(label='بحث باسم الفرع ',field_name='name', lookup_expr='icontains')
	id = CharFilter(label='بحث بكود الفرع',field_name='id', lookup_expr='icontains')
	#company = CharFilter(label='بحث بكود الفرع',field_name='company', lookup_expr='icontains')
 
	class Meta:
		model = branch
		fields = '__all__'
		exclude = ['branch_pic','phone','mobile','address','company']


		 