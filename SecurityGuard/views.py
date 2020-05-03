from django.shortcuts import redirect, render
from .models import Time
 
import datetime
from django.http import JsonResponse
from django.views.generic import ListView
from SecurityGuard.models import locations
from _datetime import timedelta
from math import atan2, cos, radians, sin, sqrt
def distance(origin, destiny):
     RADIUS = 6371 
     (latitude1, longitude1) = (origin[0], origin[1])
     (latitude2, longitude2) = (destiny[0], destiny[1])

     dLat = radians(latitude1 - latitude2)
     dLong = radians(longitude1 - longitude2)

    # matter of faith
     a = sin(dLat/2) * sin(dLat/2) + cos(radians(latitude1)) * cos(radians(latitude2)) * sin(dLong/2) * sin(dLong/2)
     c = 2 * atan2(sqrt(a), sqrt(1-a))

     return (RADIUS * c)
    

def listall(request):
     today=datetime.date.today()
     times=datetime.datetime.now()
     new_time = times - datetime.timedelta(hours=1, minutes=0)
     origin =[]
     destiny=[]
     for L in locations.objects.filter(active=True):
          present=False
          for i in Time.objects.filter(user=L.user,date=today,time__gt=new_time): 
               print(L.Lat, L.Lon)
               print(i.Lat, i.Lon)
               origin  =  (L.Lat, L.Lon)
               destiny =   (i.Lat, i.Lon)  
               actdestiny       =  distance(origin,destiny)  
               if actdestiny <= 5:
                    present=True    
          L.Present=present
          L.save()
     all_locations=locations.objects.filter(active=True)  
     context={
          'locations':all_locations
     }
     return render(request,'SecurityGuard/locations_list.html',context)
# class listall(ListView):
#      model=locations
#      template_name='SecurityGuard/all.html'
#      context_object_name='locations'
#      def get_queryset(self):
           
#           return Book.objects.filter(publisher=self.publisher)
#      def get_context_data(self, **kwargs):
#           context= super().get_context_data(**kwargs)
#           print(context)
#           return context
def mark_your_attendance(request):    
     lat = request.GET.get('lat', None)
     lon = request.GET.get('lon', None)
     today=datetime.date.today()
     time=datetime.datetime.now() 
     a=Time(user=request.user,date=today,time=time, out=False,Lon=lon,Lat=lat)
     a.save()
     data = {
             'is_taken':True   #Time.objects.filter(id__iexact=id).exists()
           }
     return JsonResponse(data)

def mark_your_attendance_out(request):
      
     lat = request.GET.get('lat', None)
     lon = request.GET.get('lon', None)
     today=datetime.date.today()
     time=datetime.datetime.now()  
     a=Time(user=request.user,date=today,time=time, out=True,Lon=lon,Lat=lat)
     a.save()
     data = {
             'is_taken':True   #Time.objects.filter(id__iexact=id).exists()
           }
     return JsonResponse(data)


def index(request):
     if request.method=='POST':
         
          return redirect('SecurityGuard/index.html')            
    
     return render(request, 'SecurityGuard/index.html' )

def default_map(request):
     # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1Ijoic2hlcmd5IiwiYSI6ImNrOWxwOXBpYTAyMXQzbXBjZHRkYXIyajQifQ.2I5qN72LageukO4-Ikx8Dw'
    return render(request, 'SecurityGuard/default.html', 
                  { 'mapbox_access_token': mapbox_access_token })
