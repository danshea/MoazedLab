#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Data models for Schizosaccharomyces pombe storage

from django.db import models

class DataFileObject(models.Model):
    datafileName        = models.CharField(max_length=100)
    dataFileDirectory   = models.CharField(max_length=156)
    dataIsPrivate       = models.BooleanField(default=True)
    dataFileTypeChoices = ((FASTA, 'fasta'),(FASTQ, 'fastq'),(SAM, 'sam'),(BAM, 'bam'),
                       (TEXT, 'txt'),)
    dataFileType        = models.CharField(choices=fileTypeChoices, default=TXT)
    