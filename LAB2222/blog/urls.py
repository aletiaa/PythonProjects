from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.players_list, name='players_list'),
]