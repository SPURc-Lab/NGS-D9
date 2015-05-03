#!/usr/bin/python
# Usage: delete_dtseq.py  <Original FASTA format file> <redundant contig name file>
# <Original FASTA format file> e.g. Dt_all_seq.fa
# <redundant contig name file> is the redundant contig name file generated from Program 3: get_gene_model.py, e.g. deleted_dtnames.txt
# Python program to filter the multiple FASTA format sequence file with the redundant contigs

import sys


def delete_dtseq():
    inFile = open(sys.argv[1], 'r')
    dtFile = open(sys.argv[2], 'r')
    outFile = open("Dt_non-redundant_seq.fa", 'w')

    dt_names = []
    for line in dtFile.readlines():
        dt_names.append([float(line.strip().split('_Transcript')[0].split('Locus_')[1]) + \
        float(line.strip().split('_')[3].split('/')[0]) / float(line.strip().split('_')[3].split('/')[1]), line.strip().split('Confidence_')[1]])
 
    dt_names.sort(key=lambda x: x[0])
    #for item in dt_names:
    #    print item
    #sys.exit(0)

    cur_dt_index = 0
    deleting = False
    breaking = False
    for line in inFile:
        if '>' in line and breaking == False:
            while cur_dt_index < len(dt_names) and dt_names[cur_dt_index][0] < float(line.strip().split('_Transcript')[0].split('Locus_')[1]) + \
                float(line.strip().split('_')[3].split('/')[0]) / float(line.strip().split('_')[3].split('/')[1]):
                cur_dt_index = cur_dt_index + 1
            if cur_dt_index >= len(dt_names):
                outFile.write(line)
                breaking = True
                continue
            elif dt_names[cur_dt_index][0] == float(line.strip().split('_Transcript')[0].split('Locus_')[1]) + \
            float(line.strip().split('_')[3].split('/')[0]) / float(line.strip().split('_')[3].split('/')[1]):# and dt_names[cur_dt_index][1] in line: 
                deleting = True
                #print dt_names[cur_dt_index][0]
                #cur_dt_index = cur_dt_index + 1
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

