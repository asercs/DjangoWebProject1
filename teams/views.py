from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpRequest
from .models import Teams
from players.models import Players

class TeamsDetailView(DetailView):
    model = Teams
    template_name = 'teams.html'
    context_object_name = 'teams'
    slug_url_kwarg = 'teamName'
    slug_field = 'teamName'

    def get_context_data(self, *args, **kwargs):
        context = super(TeamsDetailView, self).get_context_data(*args, **kwargs)
        context['players'] = Players.objects.all()
        return context

def teams_home(request):
    teams = Teams.objects.all().order_by('teamName')
    return render(request, 'teams_page.html', {
        'teams': teams
        }
    )

def teams(request):
    return render(request, 'app/index.html')

# Create your views here.
