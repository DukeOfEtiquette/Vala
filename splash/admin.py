from django.contrib import admin

from splash import models as sModels

# Register your models here.
admin.site.register(sModels.ValaEntryDate)
admin.site.register(sModels.ValaEntryEquipment)
admin.site.register(sModels.ValaEntryExperimentType)
admin.site.register(sModels.ValaEntryFile)
admin.site.register(sModels.ValaEntryFormulation)
admin.site.register(sModels.ValaEntryPageRange)
admin.site.register(sModels.ValaEntryScientist)
admin.site.register(sModels.ValaEntryStatus)
admin.site.register(sModels.ValaEntry)
