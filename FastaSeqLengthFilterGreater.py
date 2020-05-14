#!/usr/bin/python3
#FastaSeqLengthFilter.py
#This script takes milti-FASTA and an integer N as input, and filter out the FASTA by length, which means greater than N
#The output will be a new milti-FASTA with seq length <= N deleted
#Version: Y.H.S, 2020-05-14
                                                                          
import sys

def FastaSeqLengthFilter():
    fi=open(sys.argv[1],'r')
    N=int(sys.argv[2])
    
    lines=fi.readlines()
    for i in range(0,len(lines),2):
        if len(lines[i+1].strip()) > N:
            print(lines[i].strip())
            print(lines[i+1].strip())
        else:
            continue

if len(sys.argv) != 3:
    print("This script takes milti-FASTA and an integer N as input, and filter out the FASTA by length, which means greater than N")
    print("The output will be a new milti-FASTA with seq length <= N deleted")
    print("Usage: [FastaSeqLengthFilter.py] [Fasta] [N]")
else:
    FastaSeqLengthFilter()
