from django import forms
from django.core.validators import RegexValidator

project_id_validator = RegexValidator(
                regex='^[a-zA-Z]{2}-[0-9]+',
                message='Hashtag doesnt comply',
            )

class NewProject(forms.Form):
  project_id = forms.CharField(label='Project ID', max_length= 20, validators=[project_id_validator])

from django.core.exceptions import ValidationError

from models import ValaEntry, Equipment

class ValaEntryForm(forms.ModelForm):
  class Meta:
    model = ValaEntry
    fields = '__all__'

class EquipmentForm(forms.ModelForm):
  class Meta:
    model = Equipment
    fields = ['equipmentID', 'name']


  def clean_valaEntry(self):
    return self.cleaned_data['valaEntry']

  def clean_equipmentID(self):
    return self.cleaned_data['equipmentID'].lower()
