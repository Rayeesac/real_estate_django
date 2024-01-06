from django import forms
from .models import Tenant
from property.models import type_choices,Property
from django.utils.translation import ugettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'

class TenantForm(forms.ModelForm):
    proof_choices = [('adhaar', 'Adhaar Card'), ('id', 'ID Card'), ('passport', 'Passport'), ('other', 'Other')]
    document_proofs = forms.ChoiceField(choices=proof_choices, required=True)
    agreement_end_date = forms.DateField(widget=DateInput(attrs={'class':'date-picker'}),label=_("Agreement End Date"))
    monthly_rent_date = forms.DateField(widget=DateInput(attrs={'class':'date-picker'}),label=_("Monthly Rent Date"))

    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proofs', 'agreement_end_date','monthly_rent_date','property','unit','image']