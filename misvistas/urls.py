from django.urls import path
from .views import mi_template

urlpatterns = [
    path("mipagina/", mi_template),
]