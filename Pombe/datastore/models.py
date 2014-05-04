# -*- coding: utf-8 -*-

# Models for Schizosaccharomyces pombe data storage

from django.db import models
import os.path
    
class DataStore(models.Model):
    name            = models.TextField(max_length=256)
    owner           = models.TextField(max_length=256)
    group           = models.TextField(max_length=256)
    is_private      = models.BooleanField(default=True)
    creation_date   = models.DateTimeField(verbose_name='Date created')
    def __unicode__(self):
        return('{0:s}'.format(self.name))
    
class DataFileObject(models.Model):
    datastore   = models.ForeignKey(DataStore)
    name        = models.CharField(max_length=100)
    directory   = models.CharField(max_length=150)
    is_private  = models.BooleanField(default=True)
    FASTA = 'FA'
    FASTQ = 'FQ'
    SAM = 'SAM'
    BAM = 'BAM'
    TEXT = 'TXT'
    dataFileTypeChoices = ((FASTA, 'fasta'),(FASTQ, 'fastq'),(SAM, 'sam'),(BAM, 'bam'),
                           (TEXT, 'text'),)
    dataFileType        = models.CharField(max_length=3, choices=dataFileTypeChoices, default=FASTA)
    def __unicode__(self):
        return('{0:s}'.format(os.path.join(self.datastore.name,self.directory,self.name)))