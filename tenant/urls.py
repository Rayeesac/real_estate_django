from django.urls import path
from .views import TenantListView, TenantCreateView,TenantDetailView, get_units

urlpatterns = [
    path('tenants/', TenantListView.as_view(), name='tenant-list'),
    path('tenants/add/',TenantCreateView.as_view(), name='tenant-create'),
    path('tenants/<int:pk>/', TenantDetailView.as_view(), name='tenant-detail'),
    path('get_units/', get_units, name='get_units'),
]