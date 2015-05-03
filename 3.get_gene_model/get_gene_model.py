#!/usr/bin/python
# Usage get_gene_model.py <annotation file>
# <annotation file> is the protein_names.txt generated from program 2: get_annotation_protein.py
# Python program to extract the top hit of the Dt contig name for each protein name of the reference species according to the criteria of:
# 1. Best E Value (the lowest E Value), then
# 2. Best confidence (the highest confidence), then
# 3. Longest length of the sequence 
# and the non top-hit Dt names would be generated in deleted_dtnames.txt

import sys

array = [] 

def gene_model():
    inFile = open(sys.argv[1], 'r')
    dtFile = open('deleted_dtnames.txt', 'w')

    count = 0
    for line in inFile.readlines():
        if len(line.strip().split('\t')) == 4:
            array.append([line.strip().split('\t')[0], line.strip().split('\t')[1], line.strip().split('\t')[2], line.strip().split('\t')[3]]) 
        else:   
            array.append([line.strip().split('\t')[0], line.strip().split('\t')[1], line.strip().split('\t')[2], ' ']) 

    array.sort(key=lambda x: x[1])
   
    current_crname = 'cr_name'
    current_dtname = 'dt_name'
    min_evalue = 100.00
    current_proteinname = 'protein_name'
    for item in array:
        if current_crname != item[1]:
            if current_crname != 'cr_name':
                print current_dtname + '\t' + current_crname + '\t' + str(min_evalue) + '\t' + current_proteinname 
            current_crname = item[1]
            current_dtname = item[0]
            min_evalue = float(item[2])
            current_proteinname = item[3]
        elif float(item[2]) < min_evalue:
            dtFile.write(current_dtname + '\n')
            current_dtname = item[0] 
            min_evalue = float(item[2])
            current_proteinname = item[3]
        elif float(item[2]) >= min_evalue:
            dtFile.write(item[0] + '\n')

    print current_dtname + '\t' + current_crname + '\t' + str(min_evalue) + '\t' + current_proteinname
    inFile.close()
    dtFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    gene_model()
    print 'I am DONE. Please check the output. :)'
