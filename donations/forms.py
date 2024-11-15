from django import forms
from .models import DonationCollection

class DonationCollectionForm(forms.ModelForm):
    class Meta:
        model = DonationCollection
        fields ='__all__'
