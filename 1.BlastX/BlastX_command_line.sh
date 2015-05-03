#!/bin/bash
# Usage: BlastX_command_line.sh <e-value exponent> <blast-formatted db> <query file> 
# <e-value exponent> in an integer format e.g. 6 for 10e-6
# <blast-formatted db> is a valid filename of the Blast formatted protein database file
# <query file> is the FASTA format sequence file to search using BLASTX
# Bash shell script to use BlastX to search protein database using a translated nucleotide query

# Directory of Blast 2.2.30+
BLASTDIR="/home/nus/nano/ncbi-blast-2.2.30+/bin"
# BLASTX
BLASTX="blastx"
# Default values
evalue=6
db=Creinhardtii_169_peptide.fa
queryfile=Dt_all_seq.fa

# Command line
commandline="$BLASTDIR/$BLASTX -num_threads 8 -evalue 1e-${1:-$evalue} -db ${2:-$db} -query ${3:-$queryfile}"

echo $commandline
exec $commandline > blast_output.txt
