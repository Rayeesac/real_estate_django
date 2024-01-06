from django import forms
from .models import Property, Unit, type_choices

class PropertyForm(forms.ModelForm):
    rent_cost = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    unit_type = forms.ChoiceField(choices=type_choices, required=True)
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'image','features','unit_type','rent_cost']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_type', 'rent_cost']

class SearchForm(forms.Form):
    property_feature = forms.CharField(required=False)
    unit_feature = forms.CharField(required=False)