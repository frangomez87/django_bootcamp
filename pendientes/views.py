from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea 
from random import randint
# Create your views here.

def index(request):
    listita = Tarea.objects.all()
    persona = {"nombre":"francisco",
    "edad":31,
    "hobbies": ["pintar","disenar","dormir","comer", "jugar"],
    "lista_tarea": listita,
    }
    return render(request, "inicio.html", persona )

def tarea(request):
    numero= str(randint(500,999))
    repuesta = "el numero ganador es: " + numero
    return HttpResponse("Hola soy la tarea")

def info(request):
    return HttpResponse("hola soy la info")
# craer la vista/funcion tarea y conectar con la diferencia
# /tareas en el archivo urls.py
# despues ir al navegador y abrir http:....../tareas
