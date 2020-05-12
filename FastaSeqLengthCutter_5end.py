#!/usr/bin/python3
#FastaSeqLengthCutter_5end.py
#Version: Y.H.S, 2020-05-12
                                                                          
import sys

def FastaSeqLengthFilter():
    fi=open(sys.argv[1],'r')
    N=int(sys.argv[2])
    
    lines=fi.readlines()  #read all lines into array
    for i in range(0,len(lines),2):
        if len(lines[i+1].strip()) >= N:
            print(lines[i].strip())
            print(lines[i+1].strip()[0:N])
        else:
            print(lines[i].strip())
            print(lines[i+1].strip())

if len(sys.argv) != 3:
    print("This script takes milti-FASTA and an integer N as input, cut FASTA by length N from the beginning, and return the sequence with N, or if the full seq is less than N, output full seq")
    print("The output will be a new milti-FASTA with seq length <=N, lines won't change")
    print("This script cannot take multi-line FASTA, if not, please run Linearizer first.")
    print("Usage: [FastaSeqLengthCutter_5end.py] [Fasta] [N]")
else:
    FastaSeqLengthFilter()
