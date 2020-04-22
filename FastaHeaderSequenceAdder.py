#!/usr/bin/python3
#FastaHeaderSequenceAdder.py
#This script takes FASTA file as input, add the sequence to the header line, by a specific delimitor
#The delimitor can be: dot, underline, or dash
#Version: Y.H.S, 2020-04-22
                                                                          
import sys

def Main():
    fi=open(sys.argv[1],'r')
    Delimitor=str(sys.argv[2])
    fo=open(sys.argv[3],'w')

    lines=fi.readlines()
    for i in range(0,len(lines),2):
        header=lines[i].strip()
        seq=lines[i+1].strip()
        Newheader=str(header)+Delimitor+str(seq)
        fo.write(Newheader+"\n"+seq+"\n")
    fi.close()
    fo.close()

if len(sys.argv) != 4:
    print("This script takes FASTA file as input, add the sequence to the header line, by a specific delimitor")
    print("This script won't take care of the FASTA with multi-line sequence. Please run FastaSeqLinearizer.py to solve the problem")
    print("The delimitor can be: dot, underline, or dash and anything else")
    print("Usage: [FastaHeaderSequenceAdder.py] [Input.fa] [Delimitor|. or - or _] [Output.fa]")
else:
    Main()
