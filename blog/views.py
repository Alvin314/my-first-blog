from django.shortcuts import render
from django.utils import timezone
from .models import Game
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    games = Game.objects.all()
    return render(request, 'blog/post_list.html', {'games': games})
