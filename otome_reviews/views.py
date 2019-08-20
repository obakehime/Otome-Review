from django.shortcuts import render
from .models import Game

# Create your views here.


def index(request):
    """The home page for Otome Reviews."""
    return render(request, 'otome_reviews/index.html')

def games(request):
    """Show all games."""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'otome_reviews/games.html', context)

def game(request, game_id):
    """Show a single game and all of its entries."""
    game = Game.objects.get(id=game_id)
    entries = game.entry_set.order_by('-date_added')
    context = {'game': game, 'entries': entries}
    return render(request, 'otome_reviews/game.html', context)
