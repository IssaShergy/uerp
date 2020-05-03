from django.contrib import admin
from .models import Account,yearTBL,TranTable,tbcurrency,costcenter,TranTableMain
from Finance.models import Customer, Town, Weather
# Register your models here.
  

admin.site.register(yearTBL)
admin.site.register(TranTable)
admin.site.register(tbcurrency)
 
admin.site.register(TranTableMain)    
admin.site.register(Account)
admin.site.register(costcenter)

admin.site.register(Customer)


class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'county')
    ordering = ['county', 'name']


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('town', 'date')
    ordering = ['town', 'date']

admin.site.register(Town, TownAdmin)
admin.site.register(Weather, WeatherAdmin)

