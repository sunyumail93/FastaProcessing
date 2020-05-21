#!/usr/bin/python3
#This is a script to linerarize multi-line FASTA sequences. It will change the format into one-line header with one-line sequences below
#Input: Any FASTA.
#Output: FASTA with one-line header and one-line sequences below
#Version: Y.H.S, 2020-05-21
                                                                          
import sys

def FastaSeqLinearizer():
    fi=open(sys.argv[1],'r')
    fo=open(sys.argv[2],'w')
    Seq=""

    lines=fi.readlines()

    for line in fi:
        if line[0] == '>':
            fo.writelines(Seq)      #Last line before the current header
            if Seq!="": fo.writelines("\n")
            fo.writelines(line)     #Current header
            Seq=""
        else:
            Seq=Seq+line.strip()
            if line is lines[-1]:     #is: really the last line, different from ==
                fo.writelines(Seq+"\n")

    fi.close()
    fo.close()

if len(sys.argv) != 3:
    print("This is a script to linerarize multi-line FASTA sequences. It will change the format into one-line header with one-line sequences below")
    print("Usage: [FastaSeqLinearizer.py] [Fasta Input] [Fasta Output]")
else:
    FastaSeqLinearizer()
