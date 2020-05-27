#!/usr/bin/python3
#FastaSeqORFShifter.py
#Version: 2020-05-26, Y.H.S
                                                                          
import sys

def FastaSeqORFShifter():
    fi=open(sys.argv[1],'r')
    #fo=open(sys.argv[2],'w')
    
    lines=fi.readlines()
    
    for i in range(0,len(lines),2):
        print(lines[i].strip())
        print(lines[i+1].strip())
        print(lines[i].strip())
        print(lines[i+1].strip()[1:])
        print(lines[i].strip())
        print(lines[i+1].strip()[2:])

if len(sys.argv) != 2:
    print("This script takes multi-FASTA as input, and cut 0, 1, 2 from 5'-end to create three sequences consequtively")
    print("Outputs will be directly printed, and three sequences maintain same name")
    print("The result can be used to run dna_to_protein.fasta.pl")
    print("Usage: [FastaSeqORFShifter.py] [Fasta]")
else:
    FastaSeqORFShifter()
