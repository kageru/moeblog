from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    latest_post_list = Post.objects.order_by('-id')

    context = {'latest_post_list': latest_post_list}

    return render(request, 'news/news.html', context)


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    context = {'post': post}

    return render(request, 'news/details.html', context)
