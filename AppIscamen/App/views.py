from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import RECP_PUPAForm, ProduccionForm,LiberacionForm
from .models import RECP_PUPA, Produccion, Liberacion
from django.contrib import messages

def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('recp_pupa_form')  # Reemplaza 'recp_pupa_form' con la URL correcta
        else:
            messages.error(request, 'Error al iniciar sesión. Verifica tu usuario y contraseña.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



def recp_pupa_form(request):
    if request.method == 'POST':
        form = RECP_PUPAForm(request.POST)
        if form.is_valid():
            form.save()
            print("Formulario guardado exitosamente")
            return redirect('pupa_success')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = RECP_PUPAForm()

    return render(request, 'recp_pupa_form.html', {'recp_pupa_form': form})

def pupa_success(request):
    return render(request, 'carga_exitosa_pupa.html')

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
    return render(request, 'carga_exitosa_prod.html')

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
    return render(request, 'carga_exitosa_lib.html')

def recp_pupa(request):
    # Lógica para la vista de RECP PUPA
    return render(request, 'recp_pupa_form.html')

def produccion(request):
    # Lógica para la vista de PRODUCCIÓN
    return render(request, 'produccion.html')

def liberacion(request):
    # Lógica para la vista de LIBERACIÓN
    return render(request, 'liberacion.html')

def informes(request):
    # Lógica para la vista de INFORMES
    return render(request, 'informes.html')


from .forms import FiltroInformeForm

def informes(request):
    # Obtén todos los registros de cada modelo
    recp_pupa_resultados = RECP_PUPA.objects.all()
    produccion_resultados = Produccion.objects.all()
    liberacion_resultados = Liberacion.objects.all()

    # Renderiza la página con los resultados de cada modelo
    return render(
        request,
        'informes.html',
        {
            'resultados_recp_pupa': recp_pupa_resultados,
            'resultados_produccion': produccion_resultados,
            'resultados_liberacion': liberacion_resultados,
        }
    )