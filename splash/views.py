from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import ValaEntry, Equipment, File
from .forms import NewProject

def new_project(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewProject(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewProject()

    return render(request, '_base.html', {'form': form})


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
        equipment_list = Equipment.objects.all();
        file_list = File.objects.filter(valaEntry=project_entry)
        template_context = {'entry_id': entry_id,
                            'pageTitle': "Edit Vala Entry",
                            'project_entry': project_entry,
                            'equipment_list': equipment_list,
                            'file_list': file_list}
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