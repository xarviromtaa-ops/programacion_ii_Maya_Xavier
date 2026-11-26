from django.contrib import admin

from inventario.models import Categoria, Movimiento, Producto, Proveedor


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_pasillo', 'activa')
    list_filter = ('activa', 'codigo_pasillo')
    search_fields = ('nombre', 'codigo_pasillo', 'descripcion')


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ruc', 'telefono', 'correo', 'ciudad', 'fecha_registro')
    list_filter = ('ciudad', 'fecha_registro')
    search_fields = ('nombre', 'ruc', 'correo', 'ciudad')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_sku',
        'nombre',
        'categoria',
        'precio_unitario',
        'stock_actual',
        'estado',
        'fecha_ingreso',
        'creado_por',
    )
    list_filter = ('estado', 'categoria', 'fecha_ingreso')
    search_fields = ('codigo_sku', 'nombre', 'descripcion', 'categoria__nombre')
    filter_horizontal = ('proveedores',)


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = (
        'producto',
        'tipo',
        'cantidad',
        'costo_unitario',
        'fecha_movimiento',
        'motivo',
        'creado_por',
    )
    list_filter = ('tipo', 'fecha_movimiento', 'producto__categoria')
    search_fields = ('producto__nombre', 'producto__codigo_sku', 'motivo')
