from django.db import models
from django.contrib.auth.models import User

class Status( models.Model ):
    code    = models.IntegerField()
    text    = models.CharField( max_length=64 )
    class Meta:
        verbose_name_plural = "Status"

class ExperimentType( models.Model ):
    code    = models.IntegerField()
    name    = models.CharField( max_length=64 )

    def __str__(self):
        return self.name

class ValaEntry( models.Model ):
    status          = models.ForeignKey( "Status" )
    creationDate    = models.DateTimeField( auto_now_add=True, blank=True )
    projectID       = models.CharField( max_length=16, )#STUB
    reviewer        = models.CharField( max_length=256, null=True)#STUB
    scientists      = models.ManyToManyField(User)
    notebooks       = models.CharField(max_length=2048, null=True)#STUB
    class Meta:
        verbose_name_plural = "ValaEntries"

    def __str__(self):
        return self.projectID

class ExperimentDetails( models.Model ):
    valaEntry       = models.ForeignKey( "ValaEntry" )
    experimentType  = models.ForeignKey( "ExperimentType", null=True )
    hypothesis      = models.CharField( max_length=1024, default="" )


class FileType( models.Model ):
    code    = models.IntegerField()
    type    = models.CharField( max_length=64 )
    class Meta:
        verbose_name_plural = "FileTypes"


class File( models.Model ):
    valaEntry     = models.ForeignKey( "ValaEntry" )
    fileType      = models.ForeignKey( "FileType" )
    description   = models.CharField( max_length=1024 )
    fileID        = models.CharField( max_length=64 )##STUB
    name          = models.CharField( max_length=256, default="" )##STUB

class Formulation( models.Model ):
    valaEntry     = models.ForeignKey( "ValaEntry" )
    formulationID = models.CharField( max_length=256 )#STUB

class EntryDate( models.Model):
    valaEntry  = models.ForeignKey( "ValaEntry" )
    start      = models.DateTimeField( 'Creation Date' )
    end        = models.DateTimeField( 'Creation Date' )

class PageRange( models.Model):
    valaEntry  = models.ForeignKey( "ValaEntry" )
    start      = models.DateTimeField( 'Creation Date' )
    end        = models.DateTimeField( 'Creation Date' )
    notebookID = models.CharField( max_length=256 ) #STUB

class Equipment( models.Model):
    valaEntry   = models.ForeignKey( "ValaEntry" )
    equipmentID = models.CharField( max_length=256 )#STUB
    name        = models.CharField( max_length=256, default="goggles" ) #STUB
    loc         = models.CharField( max_length=256, default="here" ) #STUB
