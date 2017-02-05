from django.contrib import admin

from splash import models as sModels

# Register your models here.
admin.site.register(sModels.EntryDate)
admin.site.register(sModels.Equipment)
admin.site.register(sModels.ExperimentType)
admin.site.register(sModels.File)
admin.site.register(sModels.Formulation)
admin.site.register(sModels.PageRange)
admin.site.register(sModels.Scientist)
admin.site.register(sModels.Status)
admin.site.register(sModels.ValaEntry)
