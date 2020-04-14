#!/usr/bin/python
#FastaExtractorByPatternAtPos.py
#This is a script to extract FASTA by the pattern found from the given position
#This script is probably mainly used for Seqlogo analysis
#Input: A FASTA file
#Output: A new FASTA file containing reads when the pattern can be found at the specific position.
#The output file name will be File.Pos.Pattern.fa
#Version: Y.H.S, 2020-04-13
                                                                          
import sys

def FastaExtractorByPatternAtPos():
    fi=open(sys.argv[1],'r')
    Pattern=str(sys.argv[2])
    Pos=int(sys.argv[3])
    fo=open(sys.argv[1]+"."+str(Pos)+"."+Pattern+".fa",'w')
    
    lines=fi.readlines()  #read all lines into array
    for i in range(0,len(lines),2):
        if lines[i+1][Pos-1:Pos-1+len(Pattern)] == Pattern:
            fo.writelines(lines[i].strip()+'\n')
            fo.writelines(lines[i+1].strip()+'\n')

if len(sys.argv) != 4:
    print ("This is a script to extract FASTA by the pattern found from the given position")
    print ("This script is probably mainly used for Seqlogo analysis")
    print ("Input: A FASTA file")
    print ("Output: A new FASTA file containing reads when the pattern can be found at the specific position.")
    print ("The output file name will be File.Pos.Pattern.fa, automatically")
    print ("Usage: [FastaExtractorByPatternAtPos.py] [Fasta] [Pattern] [Pos|1-based]")
else:
    FastaExtractorByPatternAtPos()
