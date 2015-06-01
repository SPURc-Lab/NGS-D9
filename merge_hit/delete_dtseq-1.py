#!/usr/bin/python
# Usage: delete_dtseq.py  <Original FASTA format file> <redundant contig name file>
# <Original FASTA format file> e.g. Dt_all_seq.fa
# <redundant contig name file> is the redundant contig name file generated from Program 3: get_gene_model.py, e.g. deleted_dtnames.txt
# Python program to filter the multiple FASTA format sequence file with the redundant contigs
# This is especially for the merged files filtering when the Dt names are modifed from original _Transcript to _*Transcript

import sys


def delete_dtseq():
    inFile = open(sys.argv[1], 'r')
    dtFile = open(sys.argv[2], 'r')
    outFile = open("Dt_non-redundant_seq.fa", 'w')

    dt_names = []
    for line in dtFile.readlines():
        dt_names.append([int(line.strip().split('Transcript')[0].split('Locus_')[1].split('_')[0]), 
            int(line.strip().split('_')[3].split('/')[0]), 
            int(line.strip().split('Transcript')[0].split('Locus_')[1].split('_')[1]), line.split('/')[0]])
 
    dt_names.sort(key=lambda x: (x[2], x[0], x[1]))

    cur_dt_index = 0
    deleting = False
    breaking = False
    for line in inFile.readlines():
        if '>' in line and breaking == False:
            if cur_dt_index >= len(dt_names):
                outFile.write(line)
                breaking = True
                continue
            elif dt_names[cur_dt_index][3] == \
                line.replace('>','').split('/')[0]:
                deleting = True
                cur_dt_index = cur_dt_index + 1
            else:
                deleting = False
                outFile.write(line)
        elif breaking == True or deleting == False:
            outFile.write(line)     

    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    delete_dtseq()
    print 'I am DONE. Please check the output. :)'
