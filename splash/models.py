from django.db import models

class Status( models.Model ):
    code    = models.IntegerField()
    text    = models.CharField( max_length=64 )

class ExperimentType( models.Model ):
    code    = models.IntegerField()
    name    = models.CharField( max_length=64 )

class ValaEntry( models.Model ):
    hypothesis      = models.CharField( max_length=1024 )
    experimentType  = models.ForeignKey( "ExperimentType" )
    status          = models.ForeignKey( "Status" )
    creationDate    = models.DateTimeField( 'Creation Date' )
    projectID       = models.CharField( max_length=16 )#STUB
    reviewer        = models.CharField( max_length=256 )#STUB

class Scientist( models.Model ):
    valaEntry   = models.ForeignKey( "ValaEntry" )
    scientistID = models.CharField( max_length=256 )#STUB

class FileType( models.Model ):
    code    = models.IntegerField()
    type    = models.CharField( max_length=64 )

class File( models.Model ):
    valaEntry     = models.ForeignKey( "ValaEntry" )
    fileType      = models.ForeignKey( "FileType" )
    description   = models.CharField( max_length=1024 )
    fileID        = models.CharField( max_length=64 )##STUB

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
