#!/usr/bin/python3
#FastaMake2Columns.py
#This script takes fasta as input, and put the header and sequence in one line, separated by tab
#Version: Y.H.S, 2020-04-24
                                                     
import sys

def FastaMake2Columns():
    fi=open(sys.argv[1],'r')
    fo=open(sys.argv[2],'w')
    
    lines=fi.readlines()
    for i in range(0,len(lines),2):
        Header=lines[i][1:].strip()
        Seq=lines[i+1].strip()
        fo.writelines(Header+'\t'+Seq+'\n')

if len(sys.argv) != 3:
    print("This script takes fasta as input, and put the header and sequence in one line, separated by tab")
    print("The aim of this script is to make a 2-column table, espeacilly for small RNAs, in order to sort or process the sequences")
    print("Usage: [FastaMatrixer.py] [Fasta] [Output]")
else:
    FastaMake2Columns()
