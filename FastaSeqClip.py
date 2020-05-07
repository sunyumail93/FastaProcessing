#!/usr/bin/python3
#FastqSeqClip.py
#Version: Y.H.S, 2020-05-07

import sys

def FastqSeqClip():

    fi=open(sys.argv[1],'r')

    clip=int(sys.argv[2])
    
    lines=fi.readlines()

    for i in range(0,len(lines),2):
            print lines[i].strip()+'-'+str(clip)
            print lines[i+1][clip:].strip()
    fi.close()       

if len(sys.argv) !=3 :
    print("This scrip clips the left x nt from fasta file and record -x in name")
    print("Usage: [FastqSeqTrim.py] [input_fasta_file] [left_clip_nt]")
else:
    FastqSeqClip()

