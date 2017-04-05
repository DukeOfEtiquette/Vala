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
    fields = ['experimentType', 'hypothesis']
    widgets = {
      'hypothesis': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
    }

  def clean_hypothesis(self):
    return self.cleaned_data['hypothesis']

  def clean_experimentType(self):
    return self.cleaned_data['experimentType']

