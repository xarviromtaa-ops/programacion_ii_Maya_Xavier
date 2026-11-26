from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from inventario.forms.categoria_form import CategoriaForm
from inventario.models import Categoria


def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'inventario/categorias/categoria_list.html',
        {'categorias': categorias},
    )


def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    productos = categoria.productos.all()
    return render(
        request,
        'inventario/categorias/categoria_detail.html',
        {'categoria': categoria, 'productos': productos},
    )


@login_required
@permission_required('inventario.add_categoria', raise_exception=True)
def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria creada exitosamente')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(
        request,
        'inventario/categorias/formulario.html',
        {'form': form},
    )


@login_required
@permission_required('inventario.change_categoria', raise_exception=True)
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria actualizada exitosamente')
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(
        request,
        'inventario/categorias/formulario.html',
        {'form': form},
    )


@login_required
@permission_required('inventario.delete_categoria', raise_exception=True)
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria eliminada exitosamente')
        return redirect('categoria_list')
    return render(
        request,
        'inventario/categorias/categoria_confirm_delete.html',
        {'categoria': categoria},
    )
