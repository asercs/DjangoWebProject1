from django.shortcuts import render
from django.views.generic import DetailView
from .models import Market

class MarketDetailView(DetailView):
    model = Market
    template_name = 'market.html'
    context_object_name = 'market'


def market_home(request):
    market = Market.objects.all().order_by('price')
    return render(request, 'market_page.html', 
        {
            'market': market
        }
    )

def market(request):
    return render(request, 'app/index.html')
# Create your views here.
