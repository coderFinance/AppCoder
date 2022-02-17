from json import load

#Para qué el json? load?

from django.template.context import Context
from django.template import Template, loader
from django.http import HttpResponse
from django.shortcuts import render

# def inicio(request):
#     return render(request, "Inicio.html")

# def inicioConTemplate(req):

#     dic = {
#         "nombre": "Juan",
#         "apellido": "Perez"
#     }

#     plantilla = loader.get_template("Inicio.html")

#     documento = plantilla.render(dic)

#     return HttpResponse(documento)

    