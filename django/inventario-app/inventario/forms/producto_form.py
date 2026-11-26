from django import forms
from inventario.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'codigo_sku',
            'nombre',
            'descripcion',
            'categoria',
            'proveedores',
            'precio_unitario',
            'stock_actual',
            'stock_minimo',
            'estado',
            'fecha_ingreso',
        ]
        widgets = {
            'codigo_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'proveedores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(
                attrs={'class': 'form-control', 'step': '0.01'}
            ),
            'stock_actual': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d',
            ),
        }

    def clean_codigo_sku(self):
        codigo_sku = self.cleaned_data.get('codigo_sku', '').strip().upper()
        if len(codigo_sku) < 3:
            raise forms.ValidationError(
                'El codigo sku debe tener al menos 3 caracteres'
            )
        return codigo_sku

    def clean_precio_unitario(self):
        precio = self.cleaned_data.get('precio_unitario')
        if precio is not None and precio <= 0:
            raise forms.ValidationError(
                'El precio unitario debe ser mayor a 0'
            )
        return precio
