from django.template import Template, context, loader
from datetime import datetime

from django.http import HttpResponse


def mi_template(request):
    nombre = "Martin"
    
    template1 = loader.get_template("mipagina.html")
    render1 = template1.render({"nombre" : nombre})
    return HttpResponse(render1)