"""
Definition of views.
"""
from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import News
from app.models import Comment
from teams.models import Teams
from players.models import Players
from django.views.generic import DetailView
from django.db.models import Q
from .forms import CommentForm
from django.shortcuts import redirect
from django.urls import reverse
 

def handler404(request, exception):
    return render(request, "app/404.html", {})

def handler500(request, exception=None):
    return render(request, "app/500.html", {})


class NewsDetailView(DetailView):
    model = News
    template_name = 'app/post.html'
    context_object_name = 'article'
    count_hit = True

    form = CommentForm
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    search_post = request.GET.get('search')
    
    if search_post:
        news_search = News.objects.filter(Q(title__icontains=search_post) | Q(news_text__icontains=search_post))
    else:
        # If not searched, return default posts
        news_search = News.objects.all().order_by("-date")[:7]
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'news_search': news_search,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Contact us if you have any questions',
            'year':datetime.now().year,
        }
    )

def matches(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/matches.html',
        {
            'title':'matches',
            'message':'matches',
            'year':datetime.now().year,
        }
    )

def faq(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/faq.html',
        {
            'year':datetime.now().year,
        }
    )

def privacy(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/privacy.html',
        {
            'year':datetime.now().year,
        }
    )


