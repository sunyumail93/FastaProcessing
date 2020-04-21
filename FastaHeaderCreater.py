#!/usr/bin/python
#FastaHeaderCreater.py
#This script creates FASTA header by a fixed Prefix, followed by _1, _2, _3...
#This is trying to avoid problems of repetitive headers
#Version: Y.H.S, 2020-04-20
                                                                          
import sys

def Counter():
    fi=open(sys.argv[1],'r')
    Prefix=sys.argv[2]
    fo=open(sys.argv[3],'w')
    
    Counter=0
    for line in fi:
        if line.startswith(">"):
            Counter=Counter+1
            Header=">"+Prefix+"_"+str(Counter)
            fo.write(Header+"\n")
        else:
            fo.write(line.strip()+"\n")
    fi.close()
    fo.close()

if len(sys.argv) != 4:
    print("This script creates FASTA header by a fixed Prefix, followed by _1, _2, _3...")
    print("This is trying to avoid problems of repetitive headers")
    print("Usage: [FastaHeaderCreater.py] [Input.fa] [Prefix] [Output.fa]")
else:
    Counter()
