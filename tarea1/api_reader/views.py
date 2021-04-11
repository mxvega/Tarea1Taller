from django.http import HttpResponse
from django.shortcuts import render
import requests
from .forms import CharacterForm

def index(request):
    dict_html = dict()
    return render(request,'index.html', dict_html)

def season_page_bb(request):
    dict_season = dict()
    lista = list()
    episodes_bb = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    for pos in range(len(episodes_bb.json())):
        temporada = episodes_bb.json()[pos]['season']
        if temporada not in lista:
            lista.append(temporada)
    dict_season['lista_de_temporadas'] = lista
    return render(request,'BB.html', dict_season)

def season_page_bcs(request):
    dict_season = dict()
    lista = list()
    episodes_bb = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    for pos in range(len(episodes_bb.json())):
        temporada = episodes_bb.json()[pos]['season']
        if temporada not in lista:
            lista.append(temporada)
    dict_season['lista_de_temporadas'] = lista
    return render(request,'BetterCallSaul.html', dict_season)

def character_page(request):
    dict_html = dict()
    if request.method == 'POST': 
        current_character = dict(request.POST)['fname']
        nombre_normalizado2 = current_character[0].lower()
        nombre_normalizado = nombre_normalizado2.replace(' ','+', 1)
        try:
            req = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={nombre_normalizado}')
            primeros10 = req.json()
            if len(primeros10) == 10:
                buscar = 1
                offset = 10
                while buscar == 1:
                    nuevos = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={nombre_normalizado}&limit=10&offset={offset}')
                    if len(nuevos.json()) == 0:
                        buscar = 0
                    else:
                        primeros10.extend(nuevos.json())
                        offset +=10
            dict_html['sunombredepersonaje'] = primeros10
        except:
            hayErrorEnLaBusqueda = 'Hay un error en la búsqueda'
        return render(request,'character.html', dict_html)
    else:
        hayErrorEnLaBusqueda = 'Hay un error en la búsqueda'
        return render(request,'character.html', hayErrorEnLaBusqueda)

def BreakingBad_id(request, pk):
    dict_episodes_bb = dict()
    dict_episodes = dict() 
    episodios_bb = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    for pos in range(len(episodios_bb.json())):
        temporada = episodios_bb.json()[pos]['season']
        if temporada == pk:
            titulo_episodio = episodios_bb.json()[pos]['title']
            id_episodio = episodios_bb.json()[pos]['episode_id']
            dict_episodes_bb[titulo_episodio] = id_episodio
    dict_episodes['lista_episodio_id'] = dict_episodes_bb
    return render(request, 'Breaking.html', dict_episodes)   

def BetterCallSaul_id(request, pk):
    dict_episodes_bcs = dict()
    dict_episodes = dict() 
    episodios_bcs = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    for pos in range(len(episodios_bcs.json())):
        temporada = episodios_bcs.json()[pos]['season']
        if temporada == pk:
            titulo_episodio = episodios_bcs.json()[pos]['title']
            id_episodio = episodios_bcs.json()[pos]['episode_id']
            dict_episodes_bcs[titulo_episodio] = id_episodio
    dict_episodes['lista_episodio_id'] = dict_episodes_bcs
    return render(request, 'BCS.html', dict_episodes)   

def Episode_id(request, pk):
    dict_episodes_info = dict() 
    info_episodio = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/{pk}')
    dict_episodes_info['episodio_info' ] = info_episodio.json()
    return render(request, 'Episode.html', dict_episodes_info)

def Personaje_id(request, pk):
    dict_personaje_info = dict()
    pk = pk.strip()
    lista_cuotas = list()
    info_personaje = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={pk}')
    dict_personaje_info['personaje_info' ] = info_personaje.json()
    cuotas = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={pk}')
    for pos in range(len(cuotas.json())):
        cuota_personaje = cuotas.json()[pos]['quote']
        lista_cuotas.append(cuota_personaje)
    dict_personaje_info['cuota_personaje' ] = lista_cuotas
    return render(request, 'personaje.html', dict_personaje_info)


