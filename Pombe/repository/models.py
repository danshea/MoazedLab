#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Models for Schizosaccharomyces pombe data storage

from django.db import models
import os.path

class Repository(models.Model):
    name            = models.CharField(max_length=256)
    owner           = models.CharField(max_length=256)
    group           = models.CharField(max_length=256)
    is_private      = models.BooleanField(default=True)
    def __unicode__(self):
        return('{0:s}'.format(self.name))
    
class Directory(models.Model):
    repository      = models.ForeignKey(Repository)
    parent          = models.ForeignKey('self', blank=True, null=True)
    name            = models.CharField(max_length=256)
    owner           = models.CharField(max_length=256)
    group           = models.CharField(max_length=256)
    is_private      = models.BooleanField(default=True)
    def __unicode__(self):
        return('{0:s}'.format(os.path.join(self.repository.name, self.name)))
    
def filepath(instance, filename):
    return(os.path.join(instance.directory.repository.name, instance.directory.name, instance.name))

class File(models.Model):
    repository      = models.ForeignKey(Repository)
    directory       = models.ForeignKey(Directory)
    name            = models.CharField(max_length=256)
    owner           = models.CharField(max_length=256)
    group           = models.CharField(max_length=256)
    is_private      = models.BooleanField(default=True)
    resource        = models.FileField(upload_to=filepath)
    def __unicode__(self):
        return('{0:s}'.format(os.path.join(self.directory.repository.name, self.directory.name, self.name)))
