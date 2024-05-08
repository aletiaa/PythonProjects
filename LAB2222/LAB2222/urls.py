"""
URL configuration for LAB2222 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import players_list, home, add_player, teams_list, player_detail_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("players/", players_list, name='players_list'),
    path("", home, name='home'),
    path("players/add-player", add_player, name='add_player'),
    path("teams/", teams_list, name='teams_list'),
    path('players/<int:player_id>/', player_detail_view, name='player_detail'),

]
