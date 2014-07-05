#!/usr/bin/env python
'''
Name: update-reference.py
Date: 2014-07-03
Author: Dan Shea <daniel.john.shea@gmail.com>
Description:

    When inserting a gene into a reference genome we must re-compute the
    coordinates for features in the gtf file to compensate for the inserted
    gene.  This program accepts a reference feature file in GTF format and a
    file containing the feature to be inserted.
    
    Offsets for features that come after the insertion are updated to reflect
    their new coordinates in the updated reference genome.

    GTF File Format Fields
    
    Fields

    Fields must be tab-separated. Also, all but the final field in each feature
    line must contain a value; "empty" columns should be denoted with a '.'

    seqname   - name of the chromosome or scaffold; chromosome names can be given
                with or without the 'chr' prefix.
    source    - name of the program that generated this feature, or the data
                source (database or project name)
    feature   - feature type name, e.g. Gene, Variation, Similarity
    start     - Start position of the feature, with sequence numbering starting at 1.
    end       - End position of the feature, with sequence numbering starting at 1.
    score     - A floating point value.
    strand    - defined as + (forward) or - (reverse).
    frame     - One of '0', '1' or '2'. '0' indicates that the first base of the
                feature is the first base of a codon, '1' that the second base is
                the first base of a codon, and so on..
    attribute - A semicolon-separated list of tag-value pairs, providing
                additional information about each feature.
                
    Sample GFF output from Ensembl export:

X	Ensembl	Repeat	2419108	2419128	42	.	.	hid=trf; hstart=1; hend=21
X	Ensembl	Repeat	2419108	2419410	2502	-	.	hid=AluSx; hstart=1; hend=303
X	Ensembl	Repeat	2419108	2419128	0	.	.	hid=dust; hstart=2419108; hend=2419128
X	Ensembl	Pred.trans.	2416676	2418760	450.19	-	2	genscan=GENSCAN00000019335
X	Ensembl	Variation	2413425	2413425	.	+	.	
X	Ensembl	Variation	2413805	2413805	.	+	.

'''

import argparse
from Bio import SeqFeature
from Bio import SeqIO
from Bio import Seq
from BCBio import GFF
import sys

def parse_file(gfffile):
    try:
        gff = GFF.parse(gfffile)
        seqs = list()
        for seq in gff:
            seqs.append(seqs)
        return seqs
    except Exception as e:
        return None

def compute_new_offsets(ref_seqs, insert_seqs):
    pass

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('ref_file',
                            type=argparse.FileType(mode='r'),
                            help='The reference gtf file')
    argparser.add_argument('insert_file', type=argparse.FileType(mode='r'),
                            help='The file containing features to be inserted')
    argparser.add_argument('-o', default=sys.stdout,
                            type=argparse.FileType(mode='w'),
                            help='output filename (default is to stdout)')
    args = argparser.parse_args()
    
    '''
    # DEBUG - print out the argument values
    for arg in ['ref_file','insert_file','o']:
        print '{} is set to {}'.format(arg, eval('args.'+arg))
    '''
    
    # Place the parsed arguments into some variables for later use
    ref_file = args.ref_file
    insert_file = args.insert_file
    output_file = args.o
    
    # Parse the reference file
    ref_seqs = parse_file(ref_file)
    
    # Parse the insert file
    insert_seqs = parse_file(insert_file)
    
    # Compute the new offsets and then write the results of the new file to the
    # output file
    compute_new_offsets(ref_seqs, insert_seqs)
    
    # Exit cleanly
    return(0)
    
if __name__ == '__main__':
    sys.exit(main())