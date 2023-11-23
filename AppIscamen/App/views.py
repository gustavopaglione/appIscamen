from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import RECP_PUPAForm, ProduccionForm,LiberacionForm


def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Puedes redirigir a otra página después del inicio de sesión exitoso
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def recp_pupa_form(request):
    if request.method == 'POST':
        form = RECP_PUPAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Cambia 'index' a la vista que desees después de guardar el formulario
    else:
        form = RECP_PUPAForm()

    return render(request, 'recp_pupa_form.html', {'recp_pupa_form': form})

def salir(request):
    # Aquí puedes agregar lógica adicional si es necesario
    return redirect('login')

def produccion_form(request):
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produccion_success')  # Puedes cambiar 'produccion_success' al nombre de tu URL de éxito
    else:
        form = ProduccionForm()
    
    return render(request, 'produccion.html', {'produccion_form': form})

def produccion_success(request):
    return render(request, 'produccion_success.html')

def liberacion_form(request):
    if request.method == 'POST':
        form = LiberacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liberacion_success')  # Puedes cambiar 'liberacion_success' al nombre de tu URL de éxito
    else:
        form = LiberacionForm()

    return render(request, 'liberacion.html', {'liberacion_form': form})

def liberacion_success(request):
    return render(request, 'liberacion_success.html')