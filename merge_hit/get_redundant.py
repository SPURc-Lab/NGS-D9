#!/usr/bin/python
# Usage get_redundant.py <transcriptID file> or <protein file>
# <transcriptID file> is the transcriptID.txt generated from program: get_transcriptID.py
# <protein file> is the protein_names.txt file generated from program: get_protein.py
# Python program to extract the top hit of the Dt contig name for each transcriptID of the reference species (Chlre4/Crein_169) according to the criteria of:
# 1. Best E Value (the lowest E Value), then
# 2. Best confidence (the highest confidence), then
# 3. Longest length of the sequence
# and the non top-hit Dt names would be generated in deleted_dtnames.txt
# Rename the output file after each run

import sys

array = [] 

def gene_model():
    inFile = open(sys.argv[1], 'r')
    dtFile = open('deleted_dtnames.txt', 'w')

    count = 0
    for line in inFile.readlines():
            array.append([line.strip().split('\t')[0], line.strip().split('\t')[1], float(line.strip().split('\t')[2]),
                          float(line.strip().split('\t')[0].split('_')[5]), int(line.strip().split('\t')[0].split('_')[-1])]) 

    array.sort(key=lambda x: (x[1], x[2], -x[3], -x[4]))
 
    current_crname = 'cr_name'
    for item in array:
        if current_crname != item[1]:
            print item
            current_crname = item[1]
        else:
            dtFile.write(item[0] + '\n')

    inFile.close()
    dtFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    gene_model()
    print 'I am DONE. Please check the output. :)'
