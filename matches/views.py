from django.shortcuts import render
from django.views.generic import DetailView
from .models import Matches

class MatchesDetailView(DetailView):
    model = Matches
    template_name = 'matches.html'
    context_object_name = 'matches'


def matches_home(request):
    matches = Matches.objects.all().order_by('date')
    return render(request, 'matches_page.html', 
        {
            'matches': matches
        }
    )

def players(request):
    return render(request, 'app/index.html')
# Create your views here.
