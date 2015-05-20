Bag3D (Blast_Chlre4-1 - get_transcriptID.py - get_redundant.py - delete redundant Dt transcripts from Dt_all_seq.fa database
       - Dt_non-redundant_seq_Chlre4 - Blast_Chlre4-2_Chlre4 - transcriptID, geneID
                                     - Blast_Chlre4-2_169 - get_protein.py - protein_names-1 - get_redundant.py - delete redundant Dt transcripts from Dt_non-redundant_seq_Chlre4
       - Dt_non-redundant_seq_Chlre4_169 - Blast_Chlre4-2_169-2 - get_protein.py - protein_names-2
       mergeDt_annotation, namely transcriptID, geneID, protein_name to have a complete annotation file) is a series of python (and bash scripts)
programs designed to filter the multiple FASTA format sequence file from de novo assembly
with the redundant contigs and execute functional assignment for the unknown contigs.
The final output files: Dt_non-redundant_seq_Chlre4.fa (non-redundant Dt contigs) and Dt_non-redundant_all_annotation.txt (annotation information).

PROGRAMS

Bag2D consists of a total of 9 programs as listed below:

1. BlastX_command_line.sh

     Bash shell script to use BlastX to search a protein database using a translated 
     nucleotide query

2. get_transcriptID.py

     Python program to extract the transcriptID from the blastX result

3. get_redundant.py

     Python program to extract the top hit of the Dt contig name for each protein name of
     the reference species according to the E Value (the lower E Value means a better hit)
     and the non top-hit Dt names will be generated in deleted_dtnames.txt

4. delete_dtseq.py

     Python program to filter the multiple fasta formatted sequence file with the 
     redundant contigs 

5. count_geneLength.py

     Python program to count sequence length of a multiple fasta formatted single header
     line sequence file

6. get_geneID.py

     Python program to extract the geneID from the blastX result

7. get_protein.py

     Python program to extract the protein names from the blastX result 

8. mergeDt_all_annotation.py

     Python program to merge the annotation information from transcriptID, geneID, protein names

9. get_pacID.py

     Python program to extract the pacID from the blastX result 

10. mergeSpecies_all_annotaion.py

     Python program to merge the annotation information from the comparison reference species

(Using different formats of reference protein files like Chlre4_best_proteins.fasta, Creinhardtii_169_peptide.fa, Creinhardtii_281_v5.5.protein.fa
 to generate transcriptID/geneID, protein names, pacID accordingly)


EXAMPLE FILES

Dt_all_seq.fa	

     Dunaliella tertiolecta fasta sequences from de novo assembly (assembler: Velvet and Oases)

Creinhardtii_169_peptide.fa, or Chlre4_best_proteins.fasta, Creinhardtii_281_v5.5.protein.fa

     protein database of a reference species Chlamydomonas reinhardtii (the file was performed 
     the below formatdb command line prior to use:

        formatdb -i Creinhardtii_169_peptide.fa -p T

     which was also applied on all the protein database files)

Creinhardtii_169_annotation_info.txt

     annotation information of the reference protein database used beforehand


WORKFLOW

The above programs and data files are used in the context of a workflow.

Total RNA from Dunaliella tertiolecta was extracted from a pure culture
and cDNA produced using standard molecular biology techniques. 
The samples were subjected to NGS DNA sequencing using Illumina MiSeq system
inhouse, and the raw datasets submitted to Partek Flow Genomics for de novo 
sequence assembly resulting in 56926 contigs ranging from 100 nt to 17153 nt.
The Velvet-Oases program was used in this assembly with default parameters 
without merging. It generated the dataset found in Dt_all_seq.fa

As an initial step to remove redundant sequences, any reverse complements
(that match 100% full length) of contigs were removed.

To prevent any bias, we subjected the raw dataset to the following workflow
firstly to remove redundant sequences based on sequence similarity to
proteomic datasets from JGI for the following species, C. reinhardtii
(being the species with the most comprehensive annotation available), 
Csu, Olu, Vcar and Chorella.

Secondly, sequences of Dt, which had annotations thus obtained, 
were matched with GO and KEGG terms to identify genes related to specific pathways.

Thirdly, the level of RNA transcripts of Dt wildtype and D9 high
lipid producer was subsequently analysed in a separate workflow.

(Note: sequence of the vector, a bleomycin-resistance marker gene, used in the mutagenesis work
leading to the isolation of D9 D. tertiolecta  was used to blast against the Dt_all_seq.fa 
dataset but no hits. A low match of a 5' 30nt was found in the contig 
Locus_5902_Transcript_1/1_Confidence_1.000_Length_1516 which matches
Cre62.g792700.t1.1 with evalue 1e-92 to a gene annotated as
"Transducin family protein / WD-40 repeat family protein".)

BAG2D ANALYSIS METHODOLOGY

This dataset was analysed using the Bag2D workflow software developed in-house
in the manner outlined below:
              
Step 1: Program 1: BlastX_command_line.sh 6 Chlre4_best_proteins.fasta Dt_all_seq.fa (6 means the e value was set at 10^-6)
                                |
                                v
Step 2: blast_out_Chlre4-1.txt --> Program 2: get_transcriptID.py blast_out_Chlre4-1.txt
                                |             
                                v              
Step 3: transcriptID.txt --> Program 3: python get_redundant.py transcriptID.txt
                                |
                                v
Step 4: deleted_dtnames.txt --> Program 4: python delete_dtseq.py  Dt_all_seq.fa deleted_dtnames.txt
                                |
                                v
 Dt_non-redundant_seq_Chlre4.fa --> Step 5: Program 5: python count_geneLength.py Dt_non-redundant_seq_Chlre4.fa --> geneLength.txt
  |                             |                                        
  |                             v                                        
  |   Step 6a: Program 1: BlastX_command_line.sh 6 Creinhardtii_169_peptide.fa Dt_non-redundant_seq.fa 
  |                             |
  |                             v
  |        blast_out_Chlre-2_169.txt --> Program 7: python get_protein.py blast_out_Chlre4-2_169.txt Creinhardtii_169_annotation_info.txt 
  |                             |
  |                             v
  |         protein_name-1.txt --> Program 3: python get_redundant.py protein_name1.txt
  |                             |
  |                             v   
  |        deleted_dtnames2.txt --> Program 4: python delete_dtseq.py  Dt_non-redundant_seq_Chlre4.fa deleted_dtnames2.txt
  |                             |
  |                             v
  |                Dt_non-redundant_seq_Chlre4_169.fa
  |                             |
  |                             v
  |            Program 1: BlastX_command_line.sh 6 Creinhardtii_169_peptide.fa Dt_non-redundant_seq_169.fa
  |                             |
  |                             v
  |                 blast_out_Chlre4-2_169-2.txt --> Step 6a: Program 7: python get_protein.py blast_output-2_169-2.txt Creinhardtii_169_annotation_info.txt
  |                             |
  |                             v
  |                      protein_name-2.txt --------------------------------------------------------------------------------------------|
  |      Step 6b: Program 1: BlastX_command_line.sh 6 Chlre4_best_proteins.fasta Dt_non-redundant_seq_Chlre4.fa                         |
  |                         |                                                                                                           |
  |                         v                                                                                                           |
  |           blast_out_Chlre4-2_Chlre4.txt --> Program 6: python get_geneID.py blast_out_Chlre4-2_Chlre4.txt --> geneID.txt  -|
  |                         |                                                                                                           |-> Program 8: mergeDt_all_annotation.py
  |                         v                                                                                                           |                   |
  |               Program 2: python get_transcriptID.py blast_out_Chlre4-2_Chlre4.txt  -->  transcriptID.txt ---------------------------|                   v
  |                                                                                                                                                   Dt_annotation file
  |_________________________________________________________________________________________________________________________________________________________|      
                                                                                |
                                                                                v
                                                         feed into Partek Genomics Suite software (GO, KEGG)

For comparison study with more reference species,
Step 7a: Program 1: BlastX_command_line.sh 6 Creinhardtii_281_v5.5.protein.fa Dt_non-redundant_seq.fa
(note: this Dt_non-redundant_seq.fa was generated from Step 1-4 using Creinhardtii_281_v5.5.protein.fa as the protein reference)
                   |
                   v
     Cre_blast_output_v5.txt --> Step 8a: Program 9: Python get_pacID.py Cre_blast_output_v5.txt --> Cre_pacID.txt --|
Step 7b: Program 1: BlastX_command_line.sh 6 CsubellipsoideaC169_227_v2.0.protein.fa Dt_non-redundant_seq.fa         |
                   |                                                                                                 |
                   v                                                                                                 |
     Csu_blast_output_v5.txt --> Step 8b: Program 9: Python get_pacID.py Csu_blast_output_v5.txt --> Csu_pacID.txt --|
Step 7c: Program 1: BlastX_command_line.sh 6 Olucimarinus_231_v2.0.protein.fa Dt_non-redundant_seq.fa	             |
                   |                                                                                                 |
                   v                                                                                                 |
     Olu_blast_output_v5.txt --> Step 8c: Program 9: Python get_pacID.py Olu_blast_output_v5.txt --> Olu_pacID.txt --|
Step 7d: Program 1: BlastX_command_line.sh 6 Vcarteri_199_v2.0.protein.fa Dt_non-redundant_seq.fa                    |
                   |                                                                                                 |
                   v                                                                                                 |
     Vcar_blast_output_v5.txt--> Step 8d: Program 9: Python get_pacID.py Vcar_blast_output_v5.txt--> Vcar_pacID.txt--|
Step 7e: Program 1: BlastX_command_line.sh 6 Chlorella_NC64A.best_proteins.fasta Dt_non-redundant_seq.fa             |
                   |                                                                                                 |
                   v                                                                                                 |
Chlorella_blast_output_v5.txt-->Step8e: Program 9: get_pacID.py Chlorella_blast_output_v5.txt-->Chlorella_pacID.txt -|
                                                                                                                     | 
                                                                                                                     |
                                                                                                                     v 
Step 9: Program 10: Python mergeSpecies_all_annotation.py Dt_all_seq.fa Cre_pacID.txt Csu_pacID.txt Olu_pacID.txt Vcar_pacID.txt Chorella_pacID.txt
                   |
                   v
         merge_annotation_output.txt
