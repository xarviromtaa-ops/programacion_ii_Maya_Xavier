from django import forms
from inventario.models import Movimiento


class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = [
            'producto',
            'tipo',
            'cantidad',
            'costo_unitario',
            'fecha_movimiento',
            'motivo',
        ]
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'costo_unitario': forms.NumberInput(
                attrs={'class': 'form-control', 'step': '0.01'}
            ),
            'fecha_movimiento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d',
            ),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is not None and cantidad <= 0:
            raise forms.ValidationError(
                'La cantidad del movimiento debe ser mayor a 0'
            )
        return cantidad

    def clean_costo_unitario(self):
        costo = self.cleaned_data.get('costo_unitario')
        if costo is not None and costo < 0:
            raise forms.ValidationError(
                'El costo unitario no puede ser negativo'
            )
        return costo
