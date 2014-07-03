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

'''

import argparse
from Bio import SeqFeature
from Bio import SeqIO
from Bio import Seq
from BCBio import GFF
import sys

def parse_ref(ref_file):
    pass

def parse_insert(insert_file):
    pass

def compute_new_offsets(parsed_ref_file, parsed_insert_file):
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
    parsed_ref_file = parse_ref(ref_file)
    
    # Parse the insert file
    parsed_insert_file = parse_insert(insert_file)
    
    # Compute the new offsets and then write the results of the new file to the
    # output file
    compute_new_offsets(parsed_ref_file, parsed_insert_file)
    
    # Exit cleanly
    return(0)
    
if __name__ == '__main__':
    sys.exit(main())