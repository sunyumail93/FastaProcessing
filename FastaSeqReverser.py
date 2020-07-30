#!/usr/bin/python3
#This is a script to generate reverse complementary FASTA sequences from the current FASTA input
#Input: Any multi-FASTA file, but with ONE-LINE sequences.
#If the FASTA sequences are not one-line, please use FastaSeqLinearizer to convert it to one-line sequences first
#or it will only reverse complement each line, but not the full sequences
#Output: Another FASTA with sequences reverse complement
#Version: 2020-07-30, Y.H.S
                                                                          
import sys

def Complementer(String):
    StringList=list(String)
    for i in range(len(StringList)):
    #Substitution based on 'Nucleic acid notation'
    #For canonical bases:
        if StringList[i]=="A": StringList[i]="T"
        elif StringList[i]=="a": StringList[i]="t"
        elif StringList[i]=="T": StringList[i]="A"
        elif StringList[i]=="t": StringList[i]="a"
        elif StringList[i]=="G": StringList[i]="C"
        elif StringList[i]=="g": StringList[i]="c"
        elif StringList[i]=="C": StringList[i]="G"
        elif StringList[i]=="c": StringList[i]="g"
    #For degenerated bases:
        elif StringList[i]=="W": StringList[i]="S"
        elif StringList[i]=="w": StringList[i]="s"
        elif StringList[i]=="S": StringList[i]="W"
        elif StringList[i]=="s": StringList[i]="w"
        elif StringList[i]=="M": StringList[i]="K"
        elif StringList[i]=="m": StringList[i]="k"
        elif StringList[i]=="K": StringList[i]="M"
        elif StringList[i]=="k": StringList[i]="m"
        elif StringList[i]=="R": StringList[i]="Y"
        elif StringList[i]=="r": StringList[i]="y"
        elif StringList[i]=="Y": StringList[i]="R"
        elif StringList[i]=="y": StringList[i]="r"
        elif StringList[i]=="B": StringList[i]="V"
        elif StringList[i]=="b": StringList[i]="v"
        elif StringList[i]=="V": StringList[i]="B"
        elif StringList[i]=="v": StringList[i]="b"
        elif StringList[i]=="D": StringList[i]="H"
        elif StringList[i]=="d": StringList[i]="h"
        elif StringList[i]=="H": StringList[i]="D"
        elif StringList[i]=="h": StringList[i]="d"
        elif StringList[i]=="N": StringList[i]="N"
        elif StringList[i]=="n": StringList[i]="n"
        else: StringList[i]="N"
    return "".join(map(str,StringList))


def FastaSeqReverser():
    fi=open(sys.argv[1],'r')
    fo=open(sys.argv[2],'w')
    
    lines=fi.readlines()  #read all lines into array

    for line in lines:
        if line[0] == '>':
            fo.writelines(line)
        else:
            reline=line.strip()[::-1]
            relinecom=Complementer(reline)
            fo.writelines(relinecom+"\n")
    
    fi.close()
    fo.close()

if len(sys.argv) != 3:
    print("This is a script to generate reverse complementary FASTA sequences from the current FASTA input")
    print("Input: Any multi-FASTA DNA file, but with ONE-LINE sequences")
    print("If the FASTA sequences are not one-line, please use FastaSeqLinearizer to convert it to one-line sequences first")
    print("or it will only reverse complement each line, but not the full sequences")
    print("Usage: [FastaSeqReverser.py] [FASTA DNA Input] [FASTA DNA Output]")
else:
    FastaSeqReverser()
