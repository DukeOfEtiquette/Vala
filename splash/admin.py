from django.contrib import admin

from splash import models as sModels

class EntryDateManager(admin.ModelAdmin):
  fieldsets = [('Date Range', {'fields': ['start', 'end']})]

class StatusManager(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['text', 'code']})]
  list_display = ( 'text', )
  list_display_links = ('text',)
  def getText(self, obj):
    return obj.text

class ExTypeManager(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['name', 'code']})]
  list_display = ( 'getName', )
  def getName(self, obj):
    return obj.name

class ValaEntryManager(admin.ModelAdmin):
  list_display = ( 'getID', )
  def getID(self, obj):
    return obj.projectID

# Register your models here.
admin.site.register(sModels.EntryDate, EntryDateManager)

admin.site.register(sModels.Equipment)
admin.site.register(sModels.ExperimentType, ExTypeManager)
admin.site.register(sModels.File)
admin.site.register(sModels.Formulation)
admin.site.register(sModels.PageRange)
admin.site.register(sModels.Status, StatusManager)
admin.site.register(sModels.ValaEntry, ValaEntryManager)
