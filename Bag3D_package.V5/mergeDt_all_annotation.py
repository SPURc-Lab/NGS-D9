#!/usr/bin/python
# Usage mergeDt_all_annotaion.py <Original FASTA format file> <Annotation file>
# <Original FASTA format file> e.g. Dt_non-redundant_seq.fa
# <Annotation file> e.g., <transcriptID file> <geneID file> <protein_name file>
# Python program to merge the annotation information
import sys

def delete_dtseq():
    dtFile = open(sys.argv[1], 'r')
    inFile1 = open(sys.argv[2], 'r')
    inFile2 = open(sys.argv[3], 'r')
    inFile3 = open(sys.argv[4], 'r')
    #inFile4 = open(sys.argv[5], 'r')
    #inFile5 = open(sys.argv[6], 'r')
    outFile = open("Dt_non-redundant_all_annotation.txt", 'w')

    dt_base = []
    tr1 = []
    tr2 = []
    tr3 = []
    #tr4 = []
    #tr5 = []
    ptr_base = 0
    ptr1 = 1 
    ptr2 = 1
    ptr3 = 1
    #ptr4 = 1
    #ptr5 = 1
    for line in dtFile.readlines():
        if '>' in line:
            dt_base.append(line.split('>')[-1].strip())
    for line in inFile1.readlines():
        tr1.append(line.strip()) 
    for line in inFile2.readlines():
        tr2.append(line.strip())
    for line in inFile3.readlines():
        tr3.append(line.strip())
    #for line in inFile4.readlines():
    #    tr4.append(line.strip())
    #for line in inFile5.readlines():
    #    tr5.append(line.strip())

    while ptr_base < len(dt_base):
        tmp_line = dt_base[ptr_base]
        if dt_base[ptr_base] == tr1[ptr1].split()[0]: 
            tmp_line = tmp_line + '\t' + tr1[ptr1].split('\t', 1)[1].strip()
            if ptr1 < len(tr1) - 1:
                ptr1 = ptr1 + 1
        else:
            tmp_line = tmp_line + '\t'
 
        if dt_base[ptr_base] == tr2[ptr2].split()[0]: 
            tmp_line = tmp_line + '\t' + tr2[ptr2].split('\t', 1)[1].strip()
            if ptr2 < len(tr2) - 1:
                ptr2 = ptr2 + 1
        else:
            tmp_line = tmp_line + '\t'
 
        if dt_base[ptr_base] == tr3[ptr3].split()[0]:
            tmp_line = tmp_line + '\t' + tr3[ptr3].split('\t', 1)[1].strip()
            if ptr3 < len(tr3) - 1:
                ptr3 = ptr3 + 1
        else:
            tmp_line = tmp_line + '\t'

        #if dt_base[ptr_base] == tr4[ptr4].split()[0]:
        #    tmp_line = tmp_line + '\t' + tr4[ptr4].split()[1]
        #    if ptr4 < len(tr4) - 1:
        #        ptr4 = ptr4 + 1
        #else:
        #    tmp_line = tmp_line + '\t'

        #if dt_base[ptr_base] == tr5[ptr5].split()[0]:
        #    tmp_line = tmp_line + '\t' + tr5[ptr5].split()[1]
        #    if ptr5 < len(tr5) - 1:
        #        ptr5 = ptr5 + 1
        #else:
        #    tmp_line = tmp_line + '\t'

        if tmp_line.strip() != dt_base[ptr_base]:
            outFile.write(tmp_line + '\n')      
  
        ptr_base = ptr_base + 1

    dtFile.close()
    inFile1.close()
    inFile2.close()
    inFile3.close()
    #inFile4.close()
    #inFile5.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    delete_dtseq()
    print 'I am DONE. Please check the output nano :)'

