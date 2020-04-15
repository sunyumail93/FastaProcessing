#!/usr/bin/python3
#FastaGCPercentage.py
#This script gets multi-fasta input (one-line FASTA), and calculates GC percentage of that sequence.
#The output will be a two－column table, with sequence name as col1, and GC% as col2
#Version: Y.H.S, 2020-04-15

import sys

def GetGCPercentage(Seq):
    Length=len(Seq)
    CountG=Seq.count("G")
    Countg=Seq.count("g")
    CountC=Seq.count("C")
    Countc=Seq.count("c")
    Sum=CountG+Countg+CountC+Countc
    P=float(Sum)/float(Length)*100
    return(round(P,2))

def Counter():
    fi=open(sys.argv[1],'r')
    
    lines=fi.readlines()
    for line in lines:
        if line[0] == '>':
            Name=line.strip()[1:]
        else:
            Seq=line.strip()
            GCP=GetGCPercentage(Seq)
            print(Name+"\t"+str(GCP))

if len(sys.argv) != 2:
    print("This script gets multi-fasta input (one-line FASTA), and calculates GC percentage of that sequence")
    print("The output will be a two－column table, with sequence name as col1, and GC% as col2")
    print("Usage: [FastaGCPercentage.py] [Fasta]")
else:
    Counter()
