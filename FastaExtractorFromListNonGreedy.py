#! /usr/bin/env python3
#FastaExtractorFromListNonGreedy.py
#This is a short script to extract the Fasta sequence using a given list, the list should be same as the header full name (without >)
#This script can deal with the FASTA lines that contain \n at the ends (multi-line FASTA)
#Input: FASTA file
#Output: print out the header and the lines of FASTA.
#This script is to deal with the original FASTA contain duplicates, and we only want one sequence
#Version: 2020-04-14, Y.H.S

import sys

def FastaExtractorFromList():
    fi=open(sys.argv[1],'r')
    fi2=open(sys.argv[2],'r')
    lines=fi.readlines()
    FullList=fi2.readlines()
    PRINT=False

    for fulllist in FullList:
        fulllist=fulllist.strip()
        fulllist=">"+fulllist
        Count=0
        for line in lines:
            if line.startswith(">"):
                PRINT=False
            if line.strip() == fulllist and Count==0:    #Prevent print more than one time
                print (line.strip())
                PRINT=True
                Count+=1
            elif PRINT:
                print (line.strip())

if len(sys.argv) != 3:
    print ("This is a short script to extract the Fasta sequence by a given list, the list should be same as the header full name (without >)")
    print ("This script can deal with the FASTA Sequence lines that contain \\n at the ends (multi-line seq FASTA)")
    print ("This is a directly printing script")
    print ("Different from the previous script, this is a non-greedy searching, which means only output one match if it can find.")
    print ("This script is to deal with the original FASTA contain duplicates, and we only want one sequence")
    print ("usage: FastaExtractorFromListNonGreedy.py [Fasta] [List]")
else:
    FastaExtractorFromList()
