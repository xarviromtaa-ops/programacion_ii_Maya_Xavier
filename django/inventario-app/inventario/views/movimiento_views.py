from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from inventario.forms.movimiento_form import MovimientoForm
from inventario.models import Movimiento


def movimiento_list(request):
    movimientos = Movimiento.objects.select_related(
        'producto', 'producto__categoria', 'creado_por'
    ).all()
    return render(
        request,
        'inventario/movimientos/movimiento_list.html',
        {'movimientos': movimientos},
    )


def movimiento_detail(request, pk):
    movimiento = get_object_or_404(
        Movimiento.objects.select_related(
            'producto', 'producto__categoria', 'creado_por'
        ),
        pk=pk,
    )
    return render(
        request,
        'inventario/movimientos/movimiento_detail.html',
        {'movimiento': movimiento},
    )


@login_required
@permission_required('inventario.add_movimiento', raise_exception=True)
def movimiento_create(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.creado_por = request.user
            movimiento.save()
            messages.success(request, 'Movimiento creado exitosamente')
            return redirect('movimiento_list')
    else:
        form = MovimientoForm()
    return render(
        request,
        'inventario/movimientos/formulario.html',
        {'form': form},
    )


@login_required
@permission_required('inventario.change_movimiento', raise_exception=True)
def movimiento_update(request, pk):
    movimiento = get_object_or_404(Movimiento, pk=pk)
    if request.method == 'POST':
        form = MovimientoForm(request.POST, instance=movimiento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movimiento actualizado exitosamente')
            return redirect('movimiento_list')
    else:
        form = MovimientoForm(instance=movimiento)
    return render(
        request,
        'inventario/movimientos/formulario.html',
        {'form': form, 'movimiento': movimiento},
    )


@login_required
@permission_required('inventario.delete_movimiento', raise_exception=True)
def movimiento_delete(request, pk):
    movimiento = get_object_or_404(Movimiento, pk=pk)
    if request.method == 'POST':
        movimiento.delete()
        messages.success(request, 'Movimiento eliminado exitosamente')
        return redirect('movimiento_list')
    return render(
        request,
        'inventario/movimientos/movimiento_confirm_delete.html',
        {'movimiento': movimiento},
    )
