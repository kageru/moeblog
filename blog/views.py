import datetime

from django.shortcuts import render, redirect
from .models import Article
from .models import Tag
from .models import Author
from .models import Comment
# Create your views here.


def blog(request):
    tags = Tag.objects.values('name').distinct()
    articleids_and_authors = Author.objects.all()
    authors = Author.objects.values('name').distinct()

    latest_article_list = Article.objects.order_by('-pub_date')

    context = {'latest_article_list': latest_article_list,
               'tags': tags,
               'articleids_and_authors': articleids_and_authors,
               'authors': authors}

    return render(request, 'blog/blog.html', context)


def blogfilter(request, tag_name):
    tags = Tag.objects.values('name').distinct()
    articleids_and_authors = Author.objects.all()
    authors = Author.objects.values('name').distinct()

    objects_with_tag = Tag.objects.filter(name=tag_name)
    objects_with_author = Author.objects.filter(name=tag_name)

    ids_with_tag = []

    for obj in objects_with_tag:
        ids_with_tag.append(obj.article_id.id)

    for obj in objects_with_author:
        ids_with_tag.append(obj.article_id.id)

    latest_article_list = Article.objects.filter(id__in=ids_with_tag).order_by('-pub_date')

    context = {'latest_article_list': latest_article_list,
               'tags': tags,
               'filtered': True,
               'current_tag': tag_name,
               'articleids_and_authors': articleids_and_authors,
               'authors': authors}

    return render(request, 'blog/blog.html', context)


def article(request, html_name):
    article_id = Article.objects.get(htmlname=html_name)

    if request.method == 'POST':
        if str(request.POST.get("creator")) != '' and str(request.POST.get("message")) != '':
            this_comment = Comment.objects.create(author=str(request.POST.get("creator")),
                                                  content=str(request.POST.get("message")), article_id=article_id,
                                                  comment_date=datetime.datetime.now())
            this_comment.save()

            comments = Comment.objects.filter(article_id=article_id).order_by('-comment_date')

            context = {'article': article_id,'comments': comments, 'html_path':str(html_name) + ".html"}

            return redirect(request.path_info, context)

    comments = Comment.objects.filter(article_id=article_id).order_by('-comment_date')

    context = {'article': article_id,'comments': comments, 'html_path':str(html_name) + ".html"}

    return render(request, 'blog/article.html', context)
