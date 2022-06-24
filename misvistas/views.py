from django.template import Template, context, loader
from datetime import datetime

from django.http import HttpResponse

from misvistas.models import familiar


def mi_template(request):
    nombre = "Martin"
    apellido = "Baez"
    
    listadefamilia = ["Martin", "Mariela", "Marcelo", "Marianela"]
    
    martin = familiar(nombre= "martin", edad= 24)
    marianela = familiar(nombre= "marianela", edad= 26)
    marcelo = familiar(nombre= "marcelo", edad= 55)
    mariela = familiar(nombre= "mariela", edad= 50)
    martin.save()
    marianela.save()
    marcelo.save()
    mariela.save()
    
    template1 = loader.get_template("mipagina.html")
    render1 = template1.render({"nombre" : nombre, "apellido": apellido, "listafamilia":listadefamilia, "martin": martin, "marianela": marianela, "marcelo": marcelo, "mariela": mariela,})
    return HttpResponse(render1)