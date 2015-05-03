#!/usr/bin/python
# Usage get_annotation2.py <blast output file> <annotation information for the blast-formatted db>
# <blast output file> the blast_output.txt generated from program 1: BlastX_command_line.sh using Dt_non-redundant_seq.fa as the query file, e.g. Cre_blast_output_169.txt 
# <annotation information for the blast-formatted db> is the corresponding protein name for each reference gene, e.g. Creinhardtii_169_annotation_info.txt
# Python program to get the top hit (reference contig name) of the reference species for each contig from the multiple fasta formatted fasta file
# and extract their functional assignment (protein name) from the reference, and the corresponding E Value  

import sys

last_dt_name = ''

def get_protein(dt_name, cr_name, evalue, outFile):
    inFile = open(sys.argv[2], 'r') 

# Extract Functional Assignment from the Top Hit of BlastX result  
    global last_dt_name 
    for line in inFile.readlines():
        if cr_name in line:
            protein_name = line.split('\t', 9)[8].strip()
            if last_dt_name != dt_name:
                outFile.write(dt_name + '\t' + cr_name + '\t' + evalue + '\t' + protein_name + '\n') 
                last_dt_name = dt_name
           # else:
               # outFile.write('\t' + cr_name + '\t' + evalue + '\t' + protein_name + '\n')

    inFile.close()

def get_crname():
    inFile = open(sys.argv[1], 'r')
    outFile = open("protein_names.txt", 'w')

    outer_query = False
    inner_query = False
    first_newline = False
    dt_name = ''
    for line in inFile.readlines():
        if outer_query == True and inner_query == True:
             if first_newline == True:
                 if line == '\n':
                     outer_query = False
                     inner_query = False
                     first_newline = False
                     continue
                 else:
                     cr_name = line.strip().split('|')[0]
                     evalue = line.strip().split()[-1]
                     get_protein(dt_name, cr_name, evalue, outFile) 
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

    get_crname()
    print 'I am DONE. Please check the output. :)'
