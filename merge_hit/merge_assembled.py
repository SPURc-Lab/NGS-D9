#!/usr/bin/python
# Usage: merge_assembled.py <Old merged assembled file> <new assembled file> n
# n, means the no. update version
# Python program to merge the old merged assembled FASTA format sequence file with the new assembled FASTA format sequence. 

import sys

def merge():
    oldFile = open(sys.argv[1], 'r')
    newFile = open(sys.argv[2], 'r')
    outFile = open("Dt_update.fa", 'w')
    N = sys.argv[3]    

    merge_array = []
    for line in oldFile.readlines():
        merge_array.append(line)
  
    for line in newFile.readlines():
        merge_array.append(line.replace('Transcript', N + 'Transcript')) 
   
    for item in merge_array:
        outFile.write("".join(item)) 

    oldFile.close()
    newFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    merge()
    print 'I am DONE. Please check the output. :)'
