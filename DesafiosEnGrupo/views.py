from re import template
from unittest import loader

from django.http import HttpResponse


def mi_template(request):
    minombre = "Martin"
    
    template1 = loader.get_template("mipagina.html")
    render1 = template1.render({"minombre":minombre})
    return HttpResponse(render1)