from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from .models import ValaEntry, Equipment, File
from models import Status
from .forms import NewProject, EquipmentForm


class new_project(TemplateView):
  # if this is a POST request we need to process the form data
  def post(self, request):
    # create a form instance and populate it with data from the request:
    form = NewProject(request.POST)
    # check whether it's valid:
    if form.is_valid():
      newID=form.cleaned_data.get('project_id')
      status = Status.objects.get(text='New')
      newVala = ValaEntry(status=status,projectID=newID)
      newVala.save()
      # redirect to a new URL:
      return HttpResponseRedirect('/edit/'+newID)

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

  def get(self, request):
    page_title = "Vala Project Entry System"
    form = NewProject()
    entry_list = ValaEntry.objects.order_by('creationDate')
    equipment = Equipment.objects.all();
    template_context = {'pageTitle': page_title, 'entry_list': entry_list, 'equip_list': equipment,
                        'form': form, }
    return render(request, self.template_name, template_context)
  # def post(self, request):
  #   form = NewProject()
  #   return HttpResponseRedirect('/')

class editEntry(TemplateView):
    template_name='splash/edit.html'
    paginate_by = 1

    def get(self, request, entry_id):
        page_title = "Edit entry - " + entry_id
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
                            'pageTitle': page_title,
                            'project_entry': project_entry,
                            'equipment_list': equipment_list,
                            'equipform': equipForm,
                            'file_list': file_list}
        return render(request, self.template_name, template_context)

class viewEntry(TemplateView):
  template_name = 'splash/view.html'

  def get(self, request, entry_id):
    page_title = ""
    template_context = {'entry_id': entry_id, 'pageTitle': page_title}
    return render(request, self.template_name, template_context)


class reviewEntry(TemplateView):
  template_name = 'splash/review.html'

  def get(self, request, entry_id):
    page_title = ""
    template_context = {'entry_id': entry_id, 'pageTitle': page_title}
    return render(request, self.template_name, template_context)
