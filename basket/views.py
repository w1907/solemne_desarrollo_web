from django.shortcuts import render, redirect
from django.http import HttpResponse
from basket.models import Jugador, Equipo, Entrenador
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from basket.forms import EquipoForm, JugadorForm, EntrenadorForm

# Create your views here.
def inicio(request):
	return HttpResponse("Hola")

def index(request):
    data = {}

    # SELECT * FROM player
    object_list = Jugador.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'player/list_player.html'


def AgregarEquipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('listar_equipos')
    else:
        form = EquipoForm()
    nombre_template = 'agregar_equipo.html'
    return render(request, nombre_template, {'form':form})


def AgregarJugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('listar_jugadores')
    else:
        form = JugadorForm()
    nombre_template = 'agregar_jugador.html'
    return render(request, nombre_template, {'form':form})


def AgregarEntrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listar_jugadores')
    else:
        form = EntrenadorForm()
    nombre_template = 'agregar_entrenador.html'
    return render(request, nombre_template, {'form':form})


def EditarEquipo(request, equipo_id):
    equipo = Equipo.objects.get(pk=equipo_id)
    if request.method == 'GET':
        form = EquipoForm(instance=equipo)
    else:
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
        return redirect('listar_equipos')
    return render(request, 'agregar_equipo.html', {'form':form})


def EditarJugador(request, jugador_id):
    jugador = Jugador.objects.get(pk=jugador_id)
    if request.method == 'GET':
        form = JugadorForm(instance=jugador)
    else:
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
        return redirect('listar_jugadores')
    return render(request, 'agregar_jugador.html', {'form':form})


def EditarEntrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(pk=entrenador_id)
    if request.method == 'GET':
        form = EntrenadorForm(instance=entrenador)
    else:
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
        return redirect('listar_entrenadores')
    return render(request, 'agregar_entrenador.html', {'form':form})


def EliminarEquipo(request, equipo_id):
    equipo = Equipo.objects.get(pk = equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('listar_equipos')
    return render(request, 'eliminar_equipo.html', {'equipos':equipo})

def ListaJugadores(request):
    jugadores = Jugador.objects.all()
    data = {'jugadores': jugadores}
    return render(request, 'listar_jugadores.html', data)

def ListaEquipos(request):
    equipos = Equipo.objects.all()
    data = {'equipos': equipos}

    paginator = Paginator(equipos, 10)
    page = request.GET.get('page')

    try:
        data['equipos'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['equipos'] = paginator.page(1)
    except EmptyPage:
        data['equipos'] = paginator.page(paginator.num_pages)

    template_name = 'listar_equipos.html'
    return render(request, 'listar_equipos.html', data)

def ListaEntrenadores(request):
    entrenadores = Entrenador.objects.all()
    data = {'entrenadores': entrenadores}
    return render(request, 'listar_entrenadores.html', data)