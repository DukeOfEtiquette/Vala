from django.shortcuts import render

# Create your views here.

from django.template import loader


def index(request):
    #entry_list = ValaEntry.objects.order_by('creationDate')
    template = loader.get_template('splash/index.html')
    context = {'entry_list': ""}
    return render(request, template, context)
