# forms.py
from django import forms
from .models import RECP_PUPA,Produccion, Liberacion

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




class LiberacionForm(forms.ModelForm):
    class Meta:
        model = Liberacion
        fields = ['fecha_horarios', 'sector', 'temp_humedad_entrega_cajas', 'temp_humedad_ingreso_sector_liberacion', 'millones_liberados']
        widgets = {
            'fecha_horarios': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }