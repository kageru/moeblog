from django.shortcuts import render
from .models import Article
from .models import Tag
# Create your views here.


def blog(request):
    tags = Tag.objects.values('name').distinct()

    latest_article_list = Article.objects.order_by('-id')

    context = {'latest_article_list': latest_article_list,
               'tags': tags}

    return render(request, 'blog/blog.html', context)


def blogfilter(request, tag_name):
    tags = Tag.objects.values('name').distinct()

    objects_with_tag = Tag.objects.filter(name=tag_name)

    ids_with_tag = []

    for obj in objects_with_tag:
        ids_with_tag.append(obj.article_id.id)

    latest_article_list = Article.objects.filter(id__in=ids_with_tag).order_by('-id')

    context = {'latest_article_list': latest_article_list,
               'tags': tags,
               'filtered': True,
               'current_tag': tag_name}

    return render(request, 'blog/blog.html', context)