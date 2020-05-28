#!/usr/bin/python
#FastaSeqPaster.py.py
#This script takes 2 milti-FASTA files as input (the order of them need to be matched), keep the header to be same, and paste the sequences.
#This script cannot take multi-line FASTA, if not, please run FastaSeqLinearizer.py first.
#The header names of the two input files should be matched, and if not same, it only takes the header names from the first file
#Version: Y.H.S, 2020-05-27

import sys

def FastaSeqLengthFilter():
    fi1=open(sys.argv[1],'r')
    fi2=open(sys.argv[2],'r')
    
    lines1=fi1.readlines()  #read all lines into array
    lines2=fi2.readlines()
    for i in range(0,len(lines1),2):
        print(lines1[i].strip())
        print(lines1[i+1].strip()+lines2[i+1].strip())

if len(sys.argv) != 3:
    print("This script takes 2 milti-FASTA files as input (the order of them need to be matched), keep the header to be same, and paste the sequences.")
    print("This script cannot take multi-line FASTA, if not, please run Linearizer first.")
    print("The header names of the two input files should be matched, and if not same, it only takes the header names from the first file")
    print("Usage: [FastaSeqPaster.py] [Fasta1] [Fasta2]")
else:
    FastaSeqLengthFilter()
