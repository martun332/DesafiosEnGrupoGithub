from django.template import Template, context, loader
from datetime import datetime

from django.http import HttpResponse


def mi_template(request):
    nombre = "Martin"
    apellido = "Baez"
    
    listadefamilia = ["Martin", "Mariela", "Marcelo", "Marianela"]
    
    template1 = loader.get_template("mipagina.html")
    render1 = template1.render({"nombre" : nombre, "apellido": apellido, "edad": 18, "listafamilia":listadefamilia})
    return HttpResponse(render1)