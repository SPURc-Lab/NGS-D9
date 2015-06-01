#!/usr/bin/python
# Usage get_transcriptID.py <blast output file>
# <blast output file> the blast_output.txt generated from program 1: BlastX_command_line.sh using Chlre4_best_proteins.fasta as the blast-formatted db
# and Dt_non-redundant_seq.fa as the query file, e.g. Cre_blast_output_v4.txt
# Python program to extract the transcriptID from the blastX result (v4)

import sys


def get_geneid():
    inFile = open(sys.argv[1], 'r')
    outFile = open("transcriptID.txt", 'w')

    outer_query = False
    inner_query = False
    first_newline = False
    tophit = False
    dt_name = ''
    for line in inFile.readlines():
        if outer_query == True and inner_query == True:
             if first_newline == True:
                 if tophit == True:
                     outer_query = False
                     inner_query = False
                     first_newline = False
                     tophit = False
                     continue
                 else:
                     transcriptID = line.split()[0].split('|')[2] 
                     evalue = line.strip().split()[-1]
                     outFile.write(dt_name + '\t' + 'CHLREDRAFT_' + transcriptID + '\t' + evalue + '\n')
                     tophit = True
             elif line == '\n' and first_newline == False:
                 first_newline = True           
 
        elif outer_query == True and 'Sequences producing significant alignments' in line:
            inner_query = True
        elif 'Query=' in line:
            dt_name = line.strip().split()[1]
            outer_query = True
         
    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_geneid()
    print 'I am DONE. Please check the output. :)'
