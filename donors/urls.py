from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('donor_dashboard/', views.donor_dashboard, name='donor_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('list/', views.donor_list, name='donor_list'),
    path('create/', views.create_donor, name='create_donor'),
    path('update/<int:pk>/', views.update_donor, name='update_donor'),
    path('delete/<int:pk>/', views.delete_donor, name='delete_donor'),
]
