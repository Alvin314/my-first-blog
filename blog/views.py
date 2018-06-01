from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Game
from .forms import CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    games = Game.objects.all()
    return render(request, 'blog/post_list.html', {'games': games})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def add_comment_to_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.game = game
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_game.html', {'form': form})
