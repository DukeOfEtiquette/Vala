from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from .models import ValaEntry, Equipment, File
from .forms import EquipmentForm, ValaEntryForm

class save_equipment(TemplateView):
  form_class = EquipmentForm
  template_name = 'splash/edit.html'

  def post(self, request):
    print "hello"
    return HttpResponseRedirect('/edit/AA-012345/')

'''def index(request):
    entry_list = ValaEntry.objects.order_by('creationDate')
    context = {'entry_list': entry_list}
    return render(request, 'splash/index.html', context)'''

class splashIndex(TemplateView):
    template_name = "splash/index.html"
    paginate_by = 1

    def get(self, request):
        entry_list = ValaEntry.objects.order_by('creationDate')
        equipment = Equipment.objects.all()
        paginator = Paginator(entry_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
          entrypages = paginator.page(page)
        except PageNotAnInteger:
          entrypages = paginator.page(1)
        except EmptyPage:
          entrypages = paginator.page(paginator.num_pages)

        template_context = {'pageTitle' : "Vala Project Entry System",
                            'entrypages': entrypages,
                            'entry_list': entry_list,
                            'equip_list': equipment}
        return render(request, self.template_name, template_context)

class editEntry(TemplateView):
    template_name='splash/edit.html'
    paginate_by = 1

    def get(self, request, entry_id):
        project_entry = ValaEntry.objects.get(projectID=entry_id)
        equipment_list = Equipment.objects.all()
        paginator = Paginator(equipment_list, self.paginate_by)
        equipForm = EquipmentForm()

        page = self.request.GET.get('page')

        try:
          equip_list = paginator.page(page)
        except PageNotAnInteger:
          equip_list = paginator.page(1)
        except EmptyPage:
          equip_list = paginator.page(paginator.num_pages)

        file_list = File.objects.filter(valaEntry=project_entry)
        template_context = {'entry_id': entry_id,
                            'pageTitle': "Edit Vala Entry",
                            'project_entry': project_entry,
                            'equipment_list': equipment_list,
                            'equipform': equipForm,
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
