from django.shortcuts import render
from .models import Post
from .models import Comment
# Create your views here.


def index(request):
    latest_post_list = Post.objects.order_by('-id')

    context = {'latest_post_list': latest_post_list}

    return render(request, 'news/news.html', context)


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)

    context = {'post': post,
               'comments': comments}

    return render(request, 'news/details.html', context)
