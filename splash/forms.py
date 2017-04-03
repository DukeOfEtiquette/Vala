from django import forms

class NewProject(forms.Form):
  project_id = forms.CharField(label='Project ID', max_length= 20)

from django.core.exceptions import ValidationError

from models import ValaEntry, Equipment, ExperimentDetails

class ValaEntryForm(forms.ModelForm):
  class Meta:
    model = ValaEntry
    fields = '__all__'


class ExperimentDetsForm(forms.ModelForm):
  class Meta:
    model = ExperimentDetails
    fields = ['hypothesis', 'experimentType']

  def clean_hypothesis(self):
    return self.cleaned_data['hypothesis']

  def clean_experimentType(self):
    return self.cleaned_data['experimentType']





class EquipmentForm(forms.ModelForm):
  class Meta:
    model = Equipment
    fields = ['equipmentID', 'name']

  def clean_valaEntry(self):
    return self.cleaned_data['valaEntry']

  def clean_equipmentID(self):
    return self.cleaned_data['equipmentID'].lower()
