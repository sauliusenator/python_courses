from django import forms
from .models import Preke

class PrekeForm(forms.ModelForm):
    class Meta:
        model = Preke
        fields = ['pavadinimas', 'aprasymas', 'kaina', 'kategorija']