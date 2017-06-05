from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .models import ValaEntry, Equipment, File, FileType, ExperimentDetails
from models import Status
from .forms import NewProject, ExperimentDetsForm, ScientistForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

class new_project(TemplateView):
  # if this is a POST request we need to process the form data
  @method_decorator(login_required)
  def post(self, request):
    # create a form instance and populate it with data from the request:
    form = NewProject(request.POST)
    # check whether it's valid:
    if form.is_valid():
      newID=form.cleaned_data.get('project_id')
      status = Status.objects.get(text='New')
      newVala = ValaEntry(status=status,projectID=newID)
      newVala.save()
      experimentDetails = ExperimentDetails(valaEntry=newVala)
      experimentDetails.save()
      newVala.scientists.add(request.user)
      # redirect to a new URL:
      return HttpResponseRedirect(reverse('edit', args=(newID,)))


class splashIndex(TemplateView):
  template_name = "splash/index.html"

  @method_decorator(login_required(redirect_field_name='next'))
  def get(self, request):
    print(request.user)
    page_title = "Vala Project Entry System"
    form = NewProject()
    viewAll = False
    if request.GET.get('view', '') == 'all':
        entry_list = ValaEntry.objects.order_by('creationDate')
        viewAll = True
    else:
        entry_list = ValaEntry.objects.filter(scientists__username__startswith=request.user.username).order_by('creationDate')
    equipment = Equipment.objects.all();
    template_context = {
        'viewAll': viewAll,
        'pageTitle': page_title,
        'entry_list': entry_list,
        'equip_list': equipment,
        'form': form,
        'user': request.user,
    }
    return render(request, self.template_name, template_context)


class update_scientists(TemplateView):
    template_name = 'splash/edit.html'

    def post(self, request):
        try:
            print(request.POST)
        except Exception as e:
            print (e, "nothing to add")

        return HttpResponseRedirect(return_url)


class delete_file(TemplateView):
    template_name = 'splash/edit.html'

    def post(self, request):
        # sanity
        entry_id = request.POST['entry_id']

        # Construct our return URL
        return_url = '/edit/' + entry_id + '/'

        # Get the vala entry item associated with this request
        vala_entry = ValaEntry.objects.get(projectID=entry_id)
        print("deleting...")

        file_id = request.POST['file_id']
        print(file_id)
        res = File.objects.filter(fileID=file_id).delete()
        print(res)

        return HttpResponseRedirect(return_url)


class save_file(TemplateView):
    template_name = 'splash/edit.html'

    def post(self, request):
        # sanity
        entry_id = request.POST['entry_id']

        # Construct our return URL
        return_url = '/edit/' + entry_id + '/'

        # Get the vala entry item associated with this request
        vala_entry = ValaEntry.objects.get(projectID=entry_id)
        file_type = FileType.objects.get(code=0)

        try:
            # Get our file info
            id = request.POST['file_id']
            name = request.POST['file_name']

            obj, created = File.objects.get_or_create(
                valaEntry=vala_entry,
                fileType=file_type,
                description="none",
                fileID=id,
                name=name
            )
            print "Created: ", created
        except:
            print "nothing to add"

        return HttpResponseRedirect(return_url)

class delete_equipment(TemplateView):
    template_name = 'splash/edit.html'

    def post(self, request):
        # sanity
        entry_id = request.POST['entry_id']

        # Construct our return URL
        return_url = '/edit/' + entry_id + '/'

        # Get the vala entry item associated with this request
        vala_entry = ValaEntry.objects.get(projectID=entry_id)
        print("deleting...")

        equip_id = request.POST['equip_id']
        print(equip_id)
        res = Equipment.objects.filter(equipmentID=equip_id).delete()
        print(res)

        return HttpResponseRedirect(return_url)


class save_equipment(TemplateView):
    template_name = 'splash/edit.html'

    def post(self, request):
        # sanity
        entry_id = request.POST['entry_id']

        # Construct our return URL
        return_url = '/edit/' + entry_id + '/'

        # Get the vala entry item associated with this request
        vala_entry = ValaEntry.objects.get(projectID=entry_id)

        try:
            # Get our equipment info
            id = request.POST['equip_id']
            name = request.POST['equip_name']

            obj, created = Equipment.objects.get_or_create(
                valaEntry=vala_entry,
                equipmentID=id,
                name=name
            )
            print "Created: ", created

        except:
            print "nothing to add"

        return HttpResponseRedirect(return_url)

class save_scientist(TemplateView):
    template_name = 'splash/edit.html'

    def post(self, request):
        # sanity
        entry_id = request.POST['entry_id']

        # Construct our return URL
        return_url = '/edit/' + entry_id + '/'

        # Get the vala entry item associated with this request
        vala_entry = ValaEntry.objects.get(projectID=entry_id)
        username = request.POST['sci_username']

        user = User.objects.get(username=username)

        try:
            vala_entry.scientists.add(user)
            print 'added scientist'
        except:
            print "nothing to add"

        return HttpResponseRedirect(return_url)

class delete_scientist(TemplateView):
    template_name = 'splash/edit.html'

    def post(self, request):
        # sanity
        entry_id = request.POST['entry_id']

        # Construct our return URL
        return_url = '/edit/' + entry_id + '/'

        # Get the vala entry item associated with this request
        vala_entry = ValaEntry.objects.get(projectID=entry_id)
        username = request.POST['sci_username']

        user = User.objects.get(username=username)

        try:
            vala_entry.scientists.remove(user)
            print 'removed scientist'
        except:
            print "nothing to remove"

        return HttpResponseRedirect(return_url)

class editEntry(TemplateView):
    template_name='splash/edit.html'

    @method_decorator(login_required)
    def post(self, request, entry_id):
      form = ExperimentDetsForm(request.POST)
      vala_entry = ValaEntry.objects.get(projectID=entry_id)

      if form.is_valid():

        try:
          experDetails = ExperimentDetails.objects.get(valaEntry=vala_entry)
          experDetails.experimentType = form.clean_experimentType()
          experDetails.hypothesis = form.clean_hypothesis()
        except:
          experDetails = ExperimentDetails(
            valaEntry=vala_entry,
            experimentType=form.clean_experimentType(),
            hypothesis=form.clean_hypothesis()
          )

        experDetails.save()
      return HttpResponseRedirect(reverse('edit', args=(entry_id,)))

    @method_decorator(login_required)
    def get(self, request, entry_id):
      project_entry = ValaEntry.objects.get(projectID=entry_id)
      equipment_list = Equipment.objects.filter(valaEntry=project_entry)
      experiment_details = ExperimentDetails.objects.get(valaEntry=project_entry)
      scientists_in_project = project_entry.scientists.all()
      user_values = scientists_in_project.values("username")
      scientists_list = User.objects.exclude(username__in=user_values)

      try:
        details = ExperimentDetails.objects.get(valaEntry=project_entry)
        data = {'experimentType': details.experimentType, 'hypothesis': details.hypothesis}
      except:
        data = {}

      scientists = ScientistForm()
      experiment_form = ExperimentDetsForm(initial=data)
      #scientist_list = project_entry.scientists

      file_list = File.objects.filter(valaEntry=project_entry)
      template_context = {
          'entry_id': entry_id,
          'pageTitle': "Edit Vala Entry",
          'project_entry': project_entry,
          'equipment_list': equipment_list,
          'experiment_details': experiment_details,
          'experiment_form': experiment_form,
          'file_list': file_list,
          'scientist_list': scientists_list,
          'current_scientists': scientists_in_project,
      }
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


# copied get from class splashIndex
class query(TemplateView):
    template_name = 'splash/query.html'

    def get(self, request):
        page_title = "Vala Project Entry System"
        query_list = ValaEntry.objects.order_by('creationDate')
        equipment = Equipment.objects.all();
        template_context = {'pageTitle': page_title, 'query_list': query_list, 'equip_list': equipment}
        return render(request, self.template_name, template_context)

# copied get from class splashIndex
class project(TemplateView):
    template_name = 'splash/project.html'

    def get(self, request, entry_id):
        page_title = "Vala Project Summary"
        template_context = {'pageTitle': page_title}
        return render(request, self.template_name, template_context)