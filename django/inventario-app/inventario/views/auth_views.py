from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from inventario.forms.registro_form import RegistroForm


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo, _ = Group.objects.get_or_create(name='consultores')
            user.groups.add(grupo)
            login(request, user)
            messages.success(request, 'Usuatio registrado exitosamente')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'inventario/auth/registro.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    next_url = request.POST.get('next') or request.GET.get('next') or ''

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Has iniciado sesion correctamente')
            if next_url:
                return redirect(next_url)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(
        request,
        'inventario/auth/login.html',
        {'form': form, 'next': next_url},
    )


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Sesion cerrada exitosamente')
        return redirect('login')
    return redirect('home')
