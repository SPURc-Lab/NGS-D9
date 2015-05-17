#!/usr/bin/python
# Usage: count_geneLength.py <sequence file>
# <sequence file> is a FASTA format sequence file with the sequence length information in the header, e.g. Dt_non-redundant_seq.fa
# Python program to count sequence length of a multiple fasta formatted single header line sequence file

import sys

def count_gene():
    inFile = open(sys.argv[1], 'r')
    outFile = open("geneLength.txt", 'w')

    count = 0
# Extract Sequence Length from Header Line (last argument of delimiter _)
    for line in inFile.readlines():
        if '>' in line:
            count = count + 1
            seq_length = line.split('_Length_')[1].strip()
	    outFile.write(seq_length + '\n')

    inFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    count_gene()
    print 'I am DONE. Please check the output. :)'
