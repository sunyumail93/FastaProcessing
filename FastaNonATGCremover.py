#!/usr/bin/python3
#This script changes non ATGC/atgc characters to N/n
#Input: fasta, Output: fasta
#Version: Y.H.S, 2020-04-28
                                                                          
import sys

def NonATGCremover(Seq):
    Char=list(Seq)
    i=0
    for char in Char:
        i=i+1
        if ( char == "a" ) or (char== "t") or (char== "g" ) or ( char== "c" ):
            continue
        else:
            Char[i-1] = "n"
    newSeq="".join(Char)
    return newSeq

def FastaNonATGCremover():
    fi=open(sys.argv[1],'r')
    fo=open(sys.argv[2],'w')
    
    for line in fi:
        if line.startswith(">"):
            fo.writelines(line)
        else:
            newline=NonATGCremover(line.strip())
            fo.writelines(newline+"\n")
    fi.close()
    fo.close()

if len(sys.argv) != 3:
    print("This script changes non ATGC/atgc characters to N/n")
    print("Usage: [FastaNonATGCremover.py] [Input] [Output]")
else:
    FastaNonATGCremover()
