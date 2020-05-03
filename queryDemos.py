# format decimal
# easy_install pip
# pip freez
# "{:.2f}".format(23.25489654)
# '23.25'
# يجبر الكسر 

#exception 
#view.py

# from django.http import 
# from django.shortcuts import render,get_list_or_404
# from .models import  Product
# def dynamic_lookup_view(request,id)
# try:
#     obj=Product.objects.get(id=id)
# except Product.DoesNotExist:
#     raise Http404
# context={
#     "object":obj
# }    
# return render(request ,"products/product_detial.html",context)



# filters
# https://www.youtube.com/watch?v=G-Rct7Na0UQ
# #***(1)Returns all customers from customer table
# customers = Currency.objects.all()

# #(2)Returns first customer in table
# firstCustomer = Customer.objects.first()

# #(3)Returns last customer in table
# lastCustomer = Customer.objects.last()

# #(4)Returns single customer by name
# customerByName = Customer.objects.get(name='Peter Piper')

# #***(5)Returns single customer by name
# customerById = Customer.objects.get(id=4)

# #***(6)Returns all orders related to customer (firstCustomer variable set above)
# firstCustomer.order_set.all()
# Entry.objects.order_by('author', 'pub_date').distinct('author', 'pub_date')
# Entry.objects.order_by(Lower('headline').desc())
# #(7)***Returns orders customer name: (Query parent model values)
# order = Order.objects.first() 
# parentName = order.customer.name
# Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')
# #(8)***Returns products from products table with value of "Out Door" in category attribute
# products = Product.objects.filter(category="Out Door")

# #(9)***Order/Sort Objects by id
# leastToGreatest = Product.objects.all().order_by('id') 
# greatestToLeast = Product.objects.all().order_by('-id') 

    #  today=datetime.date.today()
    #  times=datetime.datetime.now()
    #  a = datetime.datetime(2017, 6, 21, 18, 25, 30) 
    #  b = datetime.datetime(2017, 5, 16, 8, 21, 10) 
  
    #  # returns a timedelta object 
    #  c = a-b  
    #  print('Difference: ', c) 
     
    #  # returns (minutes, seconds) 
    #  minutes = divmod(c.seconds, 60)  
    #  print('Difference in minutes: ', minutes[0], 'minutes', 
    #                              minutes[1], 'seconds') 

# #(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
# productsFiltered = Product.objects.filter(tags__name="Sports")

# '''
# (11)Bonus
# Q: If the customer has more than 1 ball, how would you reflect it in the database?
  
# A: Because there are many different products and this value changes constantly you would most 
# likly not want to store the value in the database but rather just make this a function we can run
# each time we load the customers profile
# '''

# #Returns the total count for number of time a "Ball" was ordered by the first customer
# ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

# #Returns total count for each product orderd
# allOrders = {}
    # def debit(self):
    #         return currency_display(-self.amount) if self.amount < 0 else ''
    # def credit(self):
    #       return currency_display(self.amount) if self.amount > 0 else ''
 
# for order in firstCustomer.order_set.all():
# 	if order.product.name in allOrders:
# 		allOrders[order.product.name] += 1
# 	else:
# 		allOrders[order.product.name] = 1

# #Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


# #RELATED SET EXAMPLE
# class ParentModel(models.Model):
# 	name = models.CharField(max_length=200, null=True)

# class ChildModel(models.Model):
# 	parent = models.ForeignKey(ParentModel)
# 	name = models.CharField(max_length=200, null=True)

# parent = ParentModel.objects.first()
# #Returns all child models related to parent
# parent.childmodel_set.all()
# python manage.py showmigrations
