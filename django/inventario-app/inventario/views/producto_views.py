from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from inventario.forms.producto_form import ProductoForm
from inventario.models import Categoria, Producto


def producto_list(request):
    productos = Producto.objects.select_related('categoria').all()
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria', '').strip()

    if pista:
        productos = productos.filter(nombre__icontains=pista)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    categorias = Categoria.objects.all()
    es_administrador = (
        request.user.is_authenticated
        and (
            request.user.groups.filter(name='administradores').exists()
            or request.user.is_superuser
        )
    )
    return render(
        request,
        'inventario/productos/producto_list.html',
        {
            'productos': productos,
            'categorias': categorias,
            'categoria_id': categoria_id,
            'es_administrador': es_administrador,
        },
    )


def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    proveedores = producto.proveedores.all()
    movimientos = producto.movimientos.all()
    es_administrador = (
        request.user.is_authenticated
        and (
            request.user.groups.filter(name='administradores').exists()
            or request.user.is_superuser
        )
    )
    return render(
        request,
        'inventario/productos/producto_detail.html',
        {
            'producto': producto,
            'proveedores': proveedores,
            'movimientos': movimientos,
            'es_administrador': es_administrador,
        },
    )


@login_required
@permission_required('inventario.add_producto', raise_exception=True)
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creado_por = request.user
            producto.save()
            form.save_m2m()
            messages.success(request, 'Producto creado exitosamente')
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(
        request,
        'inventario/productos/formulario.html',
        {'form': form},
    )


@login_required
@permission_required('inventario.change_producto', raise_exception=True)
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    es_admin = (
        request.user.groups.filter(name='administradores').exists()
        or request.user.is_superuser
    )
    if not es_admin and producto.creado_por != request.user:
        raise PermissionDenied('Solo puedes editar los productos que tu creaste')

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(
        request,
        'inventario/productos/formulario.html',
        {'form': form},
    )


@login_required
@permission_required('inventario.delete_producto', raise_exception=True)
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente')
        return redirect('producto_list')
    return render(
        request,
        'inventario/productos/producto_confirm_delete.html',
        {'producto': producto},
    )
