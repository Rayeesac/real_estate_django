from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import TenantForm 
from .models import Tenant
from property.models import Unit, Property
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

class TenantListView(ListView):
    model = Tenant
    template_name = 'tenant_list.html'

@method_decorator(login_required, name='dispatch')
class TenantCreateView(CreateView):
    template_name = 'tenant_create.html'
    form_class = TenantForm
    success_url = reverse_lazy('tenant-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()
        return context

    def form_valid(self, form):
        tenant_instance = form.save()
        
        return super().form_valid(form)

class TenantDetailView(DetailView):
    model = Tenant
    template_name = 'tenant_detail.html'

class GetUnitsView(View):
    def get(self, request, *args, **kwargs):
        property_id = request.GET.get('property_id')
        units = Unit.objects.filter(property_id=property_id)
        data = [{'id': unit.id, 'name': unit.unit_type} for unit in units]
        return JsonResponse(data, safe=False)

get_units = GetUnitsView.as_view()