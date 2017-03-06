from django import forms
from django.core.validators import RegexValidator

project_id_validator = RegexValidator(
                regex='^[a-zA-Z]{2}-[0-9]+',
                message='Hashtag doesnt comply',
            )

class NewProject(forms.Form):
  project_id = forms.CharField(label='Project ID', max_length= 20, validators=[project_id_validator])

