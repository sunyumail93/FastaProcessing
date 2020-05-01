#!/usr/bin/python3
#FastaMultiExonsCombiner.py
#This script takes multi-FASTA (converted from BED6 exon/utr blocks) as input, and combine the sequences with same gene headers 
#This can only combine adjacent FASTA, so the file has to be sorted by gene headers
#Version: Y.H.S, 2020-05-01
                                                                          
import sys

def Counter():
    fi=open(sys.argv[1],'r')
    
    lines=fi.readlines()  #read all lines into array
    Header="ZZZZZZZ"
    Seq=""
    for i in range(0,len(lines),2):
        if lines[i].strip() == Header:
            Seq=Seq+lines[i+1].strip()
        else:
            if i>1:
                print(Header)
                print(Seq)
            Header=lines[i].strip()
            Seq=lines[i+1].strip()
    print(Header)
    print(Seq)

if len(sys.argv) != 2:
    print("This script takes multi-FASTA (converted from BED6 exon/utr blocks) as input, and combine the sequences with same gene headers")
    print("This can only combine adjacent FASTA, so the file has to be sorted by gene headers")
    print("Usage: [Template.py] [Fasta]")ß
else:
    Counter()
