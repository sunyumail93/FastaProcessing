#!/usr/bin/python3
#This is a script to simplify the FASTA header line into just the first string, but eliminate the rest after the tab delimitor
#Input: milti-FASTA
#Output: milti-FASTA with simplified header name
#Version: Y.H.S, 2020-04-23
                                                                          
import sys

def FastaHeaderSimplifier():
    fi=open(sys.argv[1],'r')
    fo=open(sys.argv[2],'w')
    
    for line in fi:
        if line[0]=='>':
            fo.writelines(line.split()[0].strip()+"\n")
        else:
            fo.writelines(line.strip()+"\n")

if len(sys.argv) != 3:
    print "This is a script to simplify the FASTA header line into just the first string, but eliminate the rest after the space or tab delimitor"
    print "For exampe, it makes the header line from '>mmu-let-7g-5p MIMAT0000121 Mus musculus let-7g-5p' to '>mmu-let-7g-5p'"
    print "Usage: [FastaHeaderSimplifier.py] [Fasta Input] [FASTA Output]"
else:
    FastaHeaderSimplifier()
