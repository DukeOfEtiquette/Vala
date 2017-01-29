from django.shortcuts import render
from django.template import loader

from .models import ValaEntry


def index(request):
    entry_list = ValaEntry.objects.order_by('creationDate')
    context = {'entry_list': entry_list}
    return render(request, 'splash/index.html', context)
