#!/usr/bin/python
# Usage get_pacID.py <blast output file>
# <blast output file> the blast_output.txt generated from program 1: BlastX_command_line.sh using Creinhardtii_281_v5.5.protein.fa/ CsubellipsoideaC169_227_v2.0.protein.fa
# Olucimarinus_231_v2.0.protein.fa/ Vcarteri_199_v2.0.protein.fa/ Chlorella_NC64A.best_proteins.fasta as the blast-formatted db and Dt_non-redundant_seq.fa as the query file, 
# e.g. Cre_blast_output_v5.txt
# Python program to extract the pacID from the blastX result

import sys


def get_pacid():
    inFile = open(sys.argv[1], 'r')
    outFile = open("pacID.txt", 'w+')

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
                     pacid = line.strip()
                     outFile.write(dt_name + '\t' + pacid + '\n')
                     tophit = True
             elif line == '\n' and first_newline == False:
                 first_newline = True           
 
        elif outer_query == True and 'Sequences producing significant alignments' in line:
            inner_query = True
        elif 'Query=' in line:
            dt_name = line.strip().split()[-1]
            outer_query = True
         
    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_pacid()
    print 'I am DONE. Please check the output. :)'
