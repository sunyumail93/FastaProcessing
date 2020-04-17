# FastaProcessing
A collection of scripts for FASTA file processing

Usage of the scritps:

Fasta2ProteinTranslator_nonATG.py data/Human.cds.nonATG.fa

Fasta2ProteinTranslator.py data/Human.cds.ATG.fa

FastaContinuousHeaderGenerator.py data/Human.cds.ATG.fa

FastaExtractorByPatternAtPos.py data/Human.cds.ATG.fa ATG 1

FastaExtractorFromList.py data/Human.cds.ATG.fa data/Human.cds.ATG.list.txt

FastaExtractorFromListNonGreedy.py data/Human.cds.ATG.fa data/Human.cds.ATG.list.txt

FastaGCPercentage.py data/Human.cds.ATG.fa

FastaHeaderConcatenator.py data/Human.miRNA.fa data/Human.miRNA.conc.fa
