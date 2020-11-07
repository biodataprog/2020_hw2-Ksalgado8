#!/usr/bin/env python3

# this is a python script template
# this next line will download the file using curl

gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

import os,gzip,itertools,csv,re

# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence



if not os.path.exists(gff):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz")

if not os.path.exists(fasta):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
# after this step I kept getting message errors such as this one curl: (23) Failed writing body (0 != 14480) I would run the file on python and would receive this  if not os.path.exists(fasta):
...     os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg --- Keep struggling with loading the data into python. 
  File "<stdin>", line 2    
with gzip.open(gff,"rt") as fh:
#had I successfully loaded the data to python I would have first allowed the count_up_genes script to count the genes by 
                Gene = "ATG"
                  For row in gff: #since gff= Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz - the genome 
               if row[1] startwith(Gene)   #start scanning the first row for ATG, since ATG is the start codon, only issue i see with this is how can I be sure that all the ATG will indeed be a gene.
                  continue
                if "Gene" for row[2] #contunie to scan for ATG and count each ATG as 1
                  print(gene) # print total of ATG found, since i was unable to load the data to python i was not able to see if the script produced a number :/
    
             
    # now add code to process this
    gff = csv.reader(fh,delimiter="\t")
    for row in gff:
        if row[0].startswith("#"):
            continue
        print(row[3],row[6])
