from django import forms
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