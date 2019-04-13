from django.urls import path
from . import views


app_name = 'infrastructures'
urlpatterns = [
    path('driver/', views.DriverListView.as_view(), name='driver_list'),
    path('driver/<uuid:pk>/', views.DriverDetailView.as_view(), name='driver_detail'),
    path('driver/register/', views.DriverRegisterView.as_view(), name='driver_register'),
    path('physical/', views.PhysicalListView.as_view(), name='physical_list'),
    path('physical/<uuid:pk>/', views.PhysicalDetailView.as_view(), name='physical_detail'),
    path('physical/register/', views.PhysicalRegisterView.as_view(), name='physical_register'),
    path('virtual/', views.VirtualListView.as_view(), name='virtual_list'),
    path('virtual/<uuid:pk>/', views.VirtualDetailView.as_view(), name='virtual_detail'),
    path('virtual/register/', views.VirtualRegisterView.as_view(), name='virtual_register'),
]