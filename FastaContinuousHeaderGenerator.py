#!/usr/bin/python
#FastaContinuousHeaderGenerator.py
#This script creates fake fasta header using 1,2,3,..., just to make each header unique
#Y.H.S, 2020-04-09
                                                                          
import sys

def FastaContinuousHeaderGenerator():
    fi=open(sys.argv[1],'r')
    fo=open(sys.argv[2],'w')
    
    lines=fi.readlines()

    for i in range(0,len(lines),2):
        header=(int(i)+2)/2
        seq=lines[i+1]
        fo.writelines('>'+str(header)+'\n')
        fo.writelines(seq)
    fi.close()
    fo.close()

if len(sys.argv) != 3:
    print "This script creates fake fasta header using 1,2,3,..., just to make each header unique"
    print "Usage: [FastaContinuousHeaderGenerator.py] [Fasta] [FastaOut]"
else:
    FastaContinuousHeaderGenerator()
