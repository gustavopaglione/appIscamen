# forms.py
from django import forms
from .models import RECP_PUPA

class RECP_PUPAForm(forms.ModelForm):
    class Meta:
        model = RECP_PUPA
        fields = ['fecha', 'horarios', 'temperatura', 'litros', 'lotes']
