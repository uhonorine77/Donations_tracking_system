from django import forms
from .models import Donors

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = '__all__'