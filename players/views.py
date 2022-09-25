from django.shortcuts import render
from django.views.generic import DetailView
from .models import Players

class PlayersDetailView(DetailView):
    model = Players
    template_name = 'players.html'
    context_object_name = 'players'
    slug_url_kwarg = 'nickname'
    slug_field = 'nickname'


def players_home(request):
    players = Players.objects.all().order_by('nickname')
    return render(request, 'players_page.html', 
        {
            'players': players
        }
    )

def players(request):
    return render(request, 'app/index.html')
# Create your views here.
