from django.shortcuts import render
from .models import Article
# Create your views here.


def blog(request):
    latest_article_list = Article.objects.order_by('-id')

    context = {'latest_article_list': latest_article_list}

    return render(request, 'blog/blog.html', context)
