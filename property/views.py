from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Property, Unit
from .forms import PropertyForm , UnitForm, SearchForm
import builtins
from pdb import set_trace

builtins.st = set_trace

class Home(ListView):
    model = Property
    template_name = 'base.html'

class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'

@method_decorator(login_required, name='dispatch')
class PropertyCreateView(CreateView):
    template_name = 'property_create.html'
    form_class = PropertyForm
    success_url = reverse_lazy('property-list')

    def form_valid(self, form):
        property_instance = form.save()

        unit_form = UnitForm(self.request.POST)
        if unit_form.is_valid():
            unit_instance = unit_form.save(commit=False)
            unit_instance.property = property_instance
            unit_instance.save()

        return super().form_valid(form)

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'

def property_and_unit_search(request):
    properties = Property.objects.all()
    units = Unit.objects.all()

    if request.method == 'GET':
        search_form = SearchForm(request.GET)
        if search_form.is_valid():

            property_feature = search_form.cleaned_data.get('property_feature')
            unit_feature = search_form.cleaned_data.get('unit_feature')

            if property_feature:
                properties = properties.filter(features__icontains=property_feature)
            if unit_feature:
                properties = properties.filter(unit__features__icontains=unit_feature)

            data = properties.values('name','address','location','features','unit__rent_cost','unit__unit_type','unit__features')
    else:
        search_form = SearchForm()

    context = {
        'properties': data,
        'form': search_form,
    }

    return render(request, 'property_and_unit_search.html', context)