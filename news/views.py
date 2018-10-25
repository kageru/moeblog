import datetime
from django.shortcuts import render
from .models import Post
from .models import Comment
from .models import Author


def index(request):
    latest_post_list = Post.objects.order_by('-id')
    authors = Author.objects.all()

    context = {'latest_post_list': latest_post_list,
               'authors': authors}

    return render(request, 'news/news.html', context)


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        if str(request.POST.get("creator")) != '' and str(request.POST.get("message")) != '':
            this_comment = Comment.objects.create(author=str(request.POST.get("creator")),
                                                  content=str(request.POST.get("message")), post_id=post,
                                                  comment_date=datetime.datetime.now())
            this_comment.save()

    comments = Comment.objects.filter(post_id=post_id).order_by('-comment_date')

    context = {'post': post,
               'comments': comments}

    return render(request, 'news/details.html', context)
