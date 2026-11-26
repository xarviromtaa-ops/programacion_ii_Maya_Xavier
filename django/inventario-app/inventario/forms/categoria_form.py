from django import forms
from inventario.models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre',
            'codigo_pasillo',
            'descripcion',
            'activa',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_pasillo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre de la categoria debe tener al menos 3 caracteres'
            )
        return nombre

    def clean_codigo_pasillo(self):
        codigo = self.cleaned_data.get('codigo_pasillo', '').strip().upper()
        if len(codigo) < 2:
            raise forms.ValidationError(
                'El codigo de pasillo debe tener al menos 2 caracteres'
            )
        return codigo
