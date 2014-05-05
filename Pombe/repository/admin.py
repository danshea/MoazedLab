#!/usr/bin/env python

################################################################################
#
# Name: admin.py
# Date: 2014-05-04
# Author: dshea
# Description: register the admin interface for the repository app
#
################################################################################

from django.contrib import admin
from repository.models import Repository, Directory, File

class DirectoryInline(admin.StackedInline):
    model = Directory
    extra = 1

#class FileInline(admin.StackedInline):
#    model = File
#    extra = 3

class RepositoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['name']}),
        ('Ownership', {'fields': ['owner', 'group', 'is_private']}),
    ]
#    inlines = [DirectoryInline, FileInline]
    inlines = [DirectoryInline]

admin.site.register(Repository, RepositoryAdmin)
