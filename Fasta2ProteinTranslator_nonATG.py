#!/usr/bin/python
#Fasta2ProteinTranslator_nonATG.py
#This script takes DNA fasta seq (CDS) as input, directly translate the sequence from the 1st nt to the end, no matter whether the start codon is AUG or not
#Version: Y.H.S, 2020-04-07
                                                                          
import sys

def translate(sequence):
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

    proteinsequence = ''
    sequence=sequence.upper()
    start = 0
    if start >= 0:
        #print(start)
        SequenceRange = sequence[int(start):]
        endTAA = sequence.find('TAA')
        endTAG = sequence.find('TAG')
        endTGA = sequence.find('TGA')
        end=max(endTAA,endTAG,endTGA)
        for n in range(0,len(SequenceRange),3):
            if SequenceRange[n:n+3] in codontable:
                proteinsequence += codontable[SequenceRange[n:n+3]]
            if proteinsequence[-1] == '*':
                break
    else:
        proteinsequence += '-'
    #for n in range(0,len(cds),3):
    #    if cds[n:n+3] in codontable:
    #        proteinsequence += codontable[cds[n:n+3]]
    return(proteinsequence)

def Fasta2ProteinTranslator():
    fi=open(sys.argv[1],'r')
    lines=fi.readlines()  #read all lines into array
    for line in lines:
        if line[0] == '>':
            print(line.strip())
        else:
            seq=translate(line.strip())
            print(seq.strip())

if len(sys.argv) != 2: #if the length of argv is not equal to 2, then print warning message
    print "This script takes DNA fasta seq (CDS) as input, directly translate the sequence from the 1st nt to the end, no matter whether the start codon is AUG or not"
    print "Please make sure the input must be CDS, or it won't make sense"
    print "The sequences have correct stop codons have * at the end"
    print "Usage: [Fasta2ProteinTranslator_nonATG.py] [Fasta]"
else:
    Fasta2ProteinTranslator()
