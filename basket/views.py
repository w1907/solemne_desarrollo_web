from django.shortcuts import render, redirect
from django.http import HttpResponse
from basket.models import Jugador
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from basket.forms import EquipoForm

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
        return redirect('listar_jugadores')
    else:
        form = EquipoForm()
    nombre_template = 'agregar_equipo.html'
    return render(request, nombre_template, {'form':form})


def ListaJugadores(request):
    jugadores = Jugador.objects.all()
    data = {'jugadores': jugadores}
    return render(request, 'listar_jugadores.html', data)