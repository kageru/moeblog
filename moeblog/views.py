from django.shortcuts import render, redirect


# Create your views here.
from django.template import RequestContext


def faq(request):
    return render(request, 'faq/faq.html')


def contact(request):
    return render(request, 'contact/contact.html')


def team(request):
    return render(request, 'team/team.html')


def troll(request):
    return redirect('https://www.fbi.gov/tips')


def handler404(request):
    return render(request, '404.html', status=404)


def handler403(request):
    return render(request, '403.html', status=403)
