from django import forms
from inventario.models import Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'ruc',
            'telefono',
            'correo',
            'ciudad',
            'fecha_registro',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d',
            ),
        }

    def clean_ruc(self):
        ruc = self.cleaned_data.get('ruc', '').strip()
        if not ruc.isdigit() or len(ruc) not in (10, 13):
            raise forms.ValidationError(
                'El ruc debe contener solo numeros de 10 o 13 digitos'
            )
        return ruc
