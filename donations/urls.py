from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation_list, name='donation_list'),
    path('list/', views.donation_list, name='donation_list'),
    path('create/', views.create_donations, name='create_donation'),
    path('donor/<int:donor_id>/', views.donation_list, name='donor_donation_list'),
    path('donations/', views.donation_list, name='donation_list_overview'),
]

