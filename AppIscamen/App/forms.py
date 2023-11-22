# forms.py
from django import forms
from .models import RECP_PUPA,Produccion

class RECP_PUPAForm(forms.ModelForm):
    class Meta:
        model = RECP_PUPA
        fields = ['fecha', 'horarios', 'temperatura', 'litros', 'lotes']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['fecha', 'lotes', 'millones_procesados', 'cantidad_torres']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }