#!/usr/bin/env python

import itertools

def isheader(line):
    return line[0] == '>'

def fasta_record(f):
    for header, group in itertools.groupby(f, isheader):
        if header:
            line = group.next()
            ensembl_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield ensembl_id, sequence
 


if __name__ == "__main__":
    with open('/Users/sliang/CCNE1/Reviewd_Human_Database.fasta') as uniprot:
        for id, seq in fasta_record(uniprot):
            print '>',id
            print seq
    
