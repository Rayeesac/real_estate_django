from django.urls import path
from .views import Home, PropertyListView, PropertyDetailView, PropertyCreateView, property_and_unit_search

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('properties/', PropertyListView.as_view(), name='property-list'),
    path('properties/add/', PropertyCreateView.as_view(), name='property-create'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('property_and_unit_search/', property_and_unit_search, name='property_and_unit_search'),
]