#!/usr/bin/python3
#This is a script to add a suffix to each FASTA header
#It can only add same suffix
#Input: Any multi-FASTA
#Output: FASTA header with suffix
#Version: Y.H.S, 2020-04-24
                                                                          
import sys

def FastaHeaderSuffixer():
    fi=open(sys.argv[1],'r')
    Suffix=sys.argv[2]
    fo=open(sys.argv[3],'w')
    
    for line in fi:
        if line[0]=='>':
            fo.writelines(line.strip()+Suffix+"\n")
        else:
            fo.writelines(line)

    fi.close()
    fo.close()

if len(sys.argv) != 4:
    print("This is a script to add a same suffix to each FASTA header")
    print("Usage: [FastaHeaderSuffixer.py] [FASTA Input] [Suffix] [FASTA Output]")
else:
    FastaHeaderSuffixer()
