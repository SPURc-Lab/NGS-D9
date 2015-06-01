#!/usr/bin/python
# Usage: hit_seq.py <Non-redundant FASTA format file> <hit Dt name file>
# <Non-redundant FASTA format file> e.g. Dt_non-redundant_seq.fa
# <hit Dt name file> is the name list of the hit sequence e.g. transcriptID-2.txt
# Python program to get only the Dt multiple FASTA format sequence file that conserved (hit) with the reference species

import sys


def delete_dtseq():
    dtFile = open(sys.argv[1], 'r')
    trFile = open(sys.argv[2], 'r')
    outFile = open("Dt_hit_seq.fa", 'w')

    dt_names = []
    for line in trFile.readlines():
        dt_names.append(line.strip().split('/')[0])

    cur_dt_index = 0
    hit = False
    for line in dtFile.readlines():
        if '>' in line:
            if cur_dt_index >= len(dt_names):
                break
            elif dt_names[cur_dt_index] == \
                line.replace('>','').split('/')[0]:
                hit = True
                cur_dt_index = cur_dt_index + 1
                outFile.write(line)
            else:
                hit = False
        elif hit == True:
            outFile.write(line)     

    dtFile.close()
    trFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    delete_dtseq()
    print 'I am DONE. Please check the output. :)'
