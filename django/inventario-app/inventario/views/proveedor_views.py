from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from inventario.forms.proveedor_form import ProveedorForm
from inventario.models import Proveedor


def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(
        request,
        'inventario/proveedores/proveedor_list.html',
        {'proveedores': proveedores},
    )


def proveedor_detail(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    productos = proveedor.productos.select_related('categoria').all()
    return render(
        request,
        'inventario/proveedores/proveedor_detail.html',
        {'proveedor': proveedor, 'productos': productos},
    )


@login_required
@permission_required('inventario.add_proveedor', raise_exception=True)
def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor creado exitosamente')
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()
    return render(
        request,
        'inventario/proveedores/formulario.html',
        {'form': form},
    )


@login_required
@permission_required('inventario.change_proveedor', raise_exception=True)
def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado exitosamete')
            return redirect('proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(
        request,
        'inventario/proveedores/formulario.html',
        {'form': form, 'proveedor': proveedor},
    )


@login_required
@permission_required('inventario.delete_proveedor', raise_exception=True)
def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, 'Proveedor eliminado exitosamente')
        return redirect('proveedor_list')
    return render(
        request,
        'inventario/proveedores/proveedor_confirm_delete.html',
        {'proveedor': proveedor},
    )
