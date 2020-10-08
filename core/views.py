from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# def index(request):
#     return redirect('/agenda')
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        psw = request.POST.get('psw')
        usuario = authenticate(username=username, password=psw)
        if usuario  is not None:
            login(request, usuario)

        else:
            messages.error(request, "Usuario ou senha inválidos")

    return redirect('/')


# Create your views here.
@login_required(login_url='/login/')
def lista_eventos(request):
    # usuario = request.user
    eventos = Evento.objects.all()
    dados = {'eventos':eventos}
    return render(request, 'agenda.html', dados)