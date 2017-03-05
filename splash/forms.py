from django import forms

class NewProject(forms.Form):
  project_id = forms.CharField(label='Project ID', max_length= 20)

