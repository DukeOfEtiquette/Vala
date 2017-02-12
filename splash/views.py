from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ValaEntry, Equipment


'''def index(request):
    entry_list = ValaEntry.objects.order_by('creationDate')
    context = {'entry_list': entry_list}
    return render(request, 'splash/index.html', context)'''

class splashIndex(TemplateView):
    template_name = "splash/index.html"
    def get(self, request):
        entry_list = ValaEntry.objects.order_by('creationDate')
        equipment = Equipment.objects.all();
        template_context = {'pageTitle' : "Vala Project Entry System", 'entry_list': entry_list, 'equip_list': equipment}
        return render(request, self.template_name, template_context)

class editEntry(TemplateView):
    template_name='splash/edit.html'
    def get(self, request, entry_id):
        project_entry = ValaEntry.objects.get(projectID=entry_id)
        template_context = {'entry_id': entry_id, 'pageTitle': "Edit Vala Entry", 'project_entry': project_entry}
        return render(request, self.template_name, template_context)

class viewEntry(TemplateView):
    template_name='splash/view.html'
    def get(self, request, entry_id):
        template_context = {'entry_id': entry_id, 'pageTitle': "Edit Vala Entry"}
        return render(request, self.template_name, template_context)

class reviewEntry(TemplateView):
    template_name='splash/review.html'
    def get(self, request, entry_id):
        template_context = {'entry_id': entry_id, 'pageTitle': "Edit Vala Entry"}
        return render(request, self.template_name, template_context)
