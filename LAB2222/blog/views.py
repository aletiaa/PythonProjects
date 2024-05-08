from django.shortcuts import render
from .models import Player, Team
from .forms import PlayerForm


# Create your views here.

def players_list(request):
    players = Player.objects.all()
    return render(request, 'blog/players_list.html', {'players': players})


def teams_list(request):
    teams = Team.objects.all()
    return render(request, 'blog/teams_list.html', {'teams': teams})


def home(request):
    return render(request, 'blog/home.html', {})


def add_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
    else:
        form = PlayerForm()
    return render(request, 'blog/add_player.html', {'form': form})


def player_detail_view(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'blog/player_details.html', {'player': player})
