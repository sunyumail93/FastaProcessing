#!/usr/bin/python3
#This script simplifies the FASTA header into a single word, without delimitator
#If the header line has already met the criteria, then no change will be made
#If not, then the a _ delimitator will be added to combine all characters (substitute space or tab)
#Version: 2020-04-17, Y.H.S
                                                                          
import sys
import re

def FastaHeaderConcatenator():
    fi=open(sys.argv[1],'r')
    fo=open(sys.argv[2],'w')
    
    for line in fi:
        if line[0]=='>':
            Sub1=re.sub('\t','_',line,count=0)
            Sub2=re.sub(' ','_',Sub1,count=0)
            Sub3=re.sub('\/','_',Sub2,count=0)
            fo.writelines(Sub3)
        else:
            fo.writelines(line)
    fi.close()
    fo.close()

if len(sys.argv) != 3:
    print("This script simplifies the FASTA header into a single word, without delimitator")
    print("If the header line has already met the criteria, then no change will be made")
    print("If not, then the a _ delimitator will be added to combine all characters (substitute space or tab)")
    print("Usage: [FastaHeaderConcatenator.py] [FASTA Input] [FASTA Output]")
else:
    FastaHeaderConcatenator()
