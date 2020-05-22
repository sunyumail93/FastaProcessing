#!/usr/bin/python3
#FastaSeqNucleotideCounter_ATCG.py
#This script takes FASTA as input, and count A,T,C,G and sum of Nt.
#This script cannot take multi-line FASTA, if not, please run Linearizer first.
#Output: each line shows the name and counts of Nt: Name A T C G Sum
#Version: Y.H.S, 2020-05-22
                                                                          
import sys

def Counter():
    fi=open(sys.argv[1],'r')
    fo=open(sys.argv[2],'w')
    
    lines=fi.readlines()
    for line in lines:
        if line[0] == '>':
            Name=line.strip()
            NameCut=Name[1:]
        else:
            Seq=line.strip()
            Acount=Seq.count("A")+Seq.count("a")
            Tcount=Seq.count("T")+Seq.count("t")
            Ccount=Seq.count("C")+Seq.count("c")
            Gcount=Seq.count("G")+Seq.count("g")
            Sum=Acount+Tcount+Ccount+Gcount
            fo.write(str(NameCut)+"\t"+str(Acount)+"\t"+str(Tcount)+"\t"+str(Ccount)+"\t"+str(Gcount)+"\t"+str(Sum)+"\n")
    fi.close()
    fo.close()

if len(sys.argv) != 3:
    print("This script takes FASTA as input, and count A,T,C,G and sum of Nt.")
    print("This script cannot take multi-line FASTA, if not, please run Linearizer first.")
    print("Output: each line shows the name and counts of Nt: Name A T C G Sum")
    print("Usage: [FastaSeqNucleotideCounter_ATCG.py] [Input.fa] [Output.txt]")
else:
    Counter()
