#  local
#  git commit -a -m "Chang setting"
#  git push origin master
#  server_hostname()
#  git pull origin master

# git add erp_proj/settings/production.py erp_proj/settings/local.py   erp_proj/settings/base.py erp_proj/settings/__init__.py
# exprt to xle file 
# https://studygyaan.com/django/how-to-export-excel-file-with-django

# pip install --upgrade setuptools 
# And try again
# pip install --upgrade -r requirements.txt

# python -m ensurepip --default-pip
# pip install djangoshop-stripe


#  signals  signals
# https://stackabuse.com/using-django-signals-to-simplify-and-decouple-code/

 

#  django-simple-history
#  https://django-simple-history.readthedocs.io/en/latest/historical_model.html
# Listing 8-23 Update multiple records with a Django model with the select_for_update() method
# # Import Django model class
# from coffeehouse.stores.models import Store
# from django.db import transaction

# # Trigger atomic transaction so loop is executed in a single transaction
# with transaction.atomic():
#     store_list = Store.objects.select_for_update().filter(state='CA')
#     # Loop over each store to update and invoke save() on each entry
#     for store in store_list:
#         # Add complex update logic here for each store
#         # save() method called on each member to update
#         store.save()


# Method decorated with @transaction.atomic to ensure logic is executed in single transaction
# @transaction.atomic
# def bulk_store_updae(store_list):
#     store_list = Store.objects.select_for_update().exclude(state='CA')
#     # Loop over each store and invoke save() on each entry
#     for store in store_list:
#         # Add complex update logic here for each store
#         # save() method called on each member to update
#         store.save()        

# # Call bulk_store_update to update store records
# bulk_store_update(store_list_to_update)

# Delete multiple records with delete()
# To delete multiple records you use the delete() method and append it to a query. Listing 8-24 illustrates this process.

# Listing 8-24 Delete model records with the delete() method
# from coffeehouse.stores.models import Store

# Store.objects.filter(city='San Diego').delete()

# breakfast_items = Item.objects.filter(menu__name='Breakfast').values('name')
# Store.objects.all().update(email="contact@coffeehouse.com")
# from django.db import transaction

# class MyView(View):
#     def post(self, request, *args, **kwargs):
#         sid = transaction.savepoint()
#         some_object = SomeModel(...)
#         some_object.save()

#         if something:
#             transaction.savepoint_rollback(sid)
#         else:
#             try:
#                 # In worst case scenario, this might fail too
#                 transaction.savepoint_commit(sid)
#             except IntegrityError:
#                 transaction.savepoint_rollback(sid)

# from django.db import transaction

# @transaction.atomic
# def make_db_stuff():

#     # do stuff in your db (inserts or whatever)

#     if success:
#         return True
#     else:
#         transaction.set_rollback(True)
#         return False

# def viewfunc(request):
#     # This code executes in autocommit mode (Django's default).
#     do_stuff()

#     with transaction.atomic():
#         # This code executes inside a transaction.
#         do_more_stuff()

# ---------------------------------k
# def __init__(self, *args, **kwargs):
        #  create a user attribute and take it out from kwargs
        # so it doesn't messes up with the other formset kwargs
        # self.businessprofile_id = kwargs.pop('businessprofile_id')
        # super(UserFormSet, self).__init__(*args, **kwargs)
        # for form in self.forms:
        #     form.empty_permitted = False
 # ------------------k
# {{ journal_entry.created_at|date:"m/d/Y" }}
#  Pagination with Class-Based Views
# def inlineformset_factory(parent_model, model, form=ModelForm,
#                           formset=BaseInlineFormSet, fk_name=None,
#                           fields=None, exclude=None, extra=3, can_order=False,
#                           can_delete=True, max_num=None, formfield_callback=None,
#                           widgets=None, validate_max=False, localized_fields=None,
#                           labels=None, help_texts=None, error_messages=None,
#                           min_num=None, validate_min=False, field_classes=None):
# views.py

# class UserListView(ListView):
#     model = User
#     template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'users'  # Default: object_list
#     paginate_by = 10
#     queryset = User.objects.all()  # Default: Model.objects.all()

# user_list.html

# <table class="table table-bordered">
#   <thead>
#     <tr>
#       <th>Username</th>
#       <th>First name</th>
#       <th>Email</th>
#     </tr>
#   </thead>
#   <tbody>
#     {% for user in users %}
#       <tr>
#         <td>{{ user.username }}</td>
#         <td>{{ user.first_name }}</td>
#         <td>{{ user.email }}</td>
#       </tr>
#     {% endfor %}
#   </tbody>
# </table>

# {% if is_paginated %}
#   <ul class="pagination">
#     {% if page_obj.has_previous %}
#       <li><a href="?page={{ page_obj.previous_page_number }}">&laquo;</a></li>
#     {% else %}
#       <li class="disabled"><span>&laquo;</span></li>
#     {% endif %}
#     {% for i in paginator.page_range %}
#       {% if page_obj.number == i %}
#         <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
#       {% else %}
#         <li><a href="?page={{ i }}">{{ i }}</a></li>
#       {% endif %}
#     {% endfor %}
#     {% if page_obj.has_next %}
#       <li><a href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
#     {% else %}
#       <li class="disabled"><span>&raquo;</span></li>
#     {% endif %}
#   </ul>
# {% endif %}
#--------------------------------------------------------------------- 
# Django 2.1 - Implement Plug-In DataTable - jQuery
# https://www.youtube.com/watch?v=_VcP_01LxMc

#Date format 
#<p>Birthday: {{ birthday|date:"M d, Y" }}</p>
