from django.db import models

class ValaEntryStatus( models.Model ):
    code    = models.IntegerField()
    string  = models.CharField( max_length=64 )

class ValaEntryExperimentType( models.Model ):
    code    = models.IntegerField()
    string  = models.CharField( max_length=64 )

class ValaEntry( models.Model ):
    hypothesis      = models.CharField( max_length=1024 )
    experimentType  = models.ForeignKey( ValaEntryExperimentType )
    status          = models.ForeignKey( ValaEntryStatus )
    creationDate    = models.DateTimeField( 'Creation Date' )
    projectID       = models.CharField( max_length=16 )#
    reviewer        = models.CharField( max_length=256 )#

class ValaEntryScientist( models.Model ):
    valaEntry   = models.ForeignKey( ValaEntry )
    scientistID = models.CharField( max_length=256 )#

class ValaEntryFileType( models.Model ):
    code    = models.IntegerField()
    string  = models.CharField( max_length=64 )

class ValaEntryFile( models.Model ):
    valaEntry     = models.ForeignKey( ValaEntry )
    fileType      = models.ForeignKey( ValaEntryFileType )
    description   = models.CharField( max_length=1024 )
    fileID        = models.CharField( max_length=64 )#

class ValaEntryFormulation( models.Model ):
    valaEntry     = models.ForeignKey( ValaEntry )
    formulationID = models.CharField( max_length=256 )#

class ValaEntryDate( models.Model):
    valaEntry  = models.ForeignKey( ValaEntry )
    start      = models.DateTimeField( 'Creation Date' )
    end        = models.DateTimeField( 'Creation Date' )

class ValaEntryPageRange( models.Model):
    valaEntry  = models.ForeignKey( ValaEntry )
    start      = models.DateTimeField( 'Creation Date' )
    end        = models.DateTimeField( 'Creation Date' )
    notebookID = models.CharField( max_length=256 ) #

class ValaEntryEquipment( models.Model):
    valaEntry   = models.ForeignKey( ValaEntry )
    equipmentID = models.CharField( max_length=256 )#
