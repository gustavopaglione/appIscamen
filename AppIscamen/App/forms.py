# forms.py
from django import forms
from .models import RECP_PUPA,Produccion, Liberacion

class RECP_PUPAForm(forms.ModelForm):
    class Meta:
        model = RECP_PUPA
        fields = ['fecha', 'horarios', 'temperatura', 'litros', 'lotes']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'horarios': forms.TimeInput(format='%H:%M'),
        }
        input_formats = ['%H:%M']


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


class FiltroInformeForm(forms.Form):
    PERIODO_CHOICES = (
        ('hoy', 'Hoy'),
        ('semana', 'Esta semana'),
        ('mes', 'Este mes'),
        # Agrega más opciones según tus necesidades
    )

    fecha_inicio = forms.DateField(label='Fecha de inicio', required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(label='Fecha de fin', required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    categoria = forms.ChoiceField(label='Categoría', choices=[('RECP_PUPA', 'RECP PUPA'), ('Produccion', 'Producción'), ('Liberacion', 'Liberación')])  # Ajusta según tus modelos