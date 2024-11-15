from django.contrib import admin
from django.urls import path, include 
from donors import views as donor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', donor_views.index, name='index'),
    path('donors/', include('donors.urls')),
    path('donations/', include('donations.urls')),
]
