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

FastaHeaderCreater.py data/Human.cds.ATG.fa Human data/Human.cds.ATG.order.fa

FastaHeaderSequenceAdder.py data/Human.miRNA.conc.fa  _ data/Human.miRNA.concseq.fa

FastaHeaderSimplifier.py data/Human.miRNA.conc.fa data/Human.miRNA.simplified.fa

FastaHeaderSuffixer.py data/Human.miRNA.conc.fa Suffix data/Human.miRNA.suffix.fa

FastaMake2Columns.py data/Human.miRNA.fa data/Human.miRNA.2column.txt

FastaMultiExonsCombiner.py data/Human.miRNA.fa

FastaNonATGCremover.py data/Human.miRNA.fa data/Human.miRNA.nonATCG.fa

FastaSeqClip.py data/Human.miRNA.fa 3

FastaSeqLengthCutter_3end.py data/Human.miRNA.fa 3

FastaSeqLengthCutter_5end.py data/Human.miRNA.fa 3

FastaSeqLengthFilterGreater.py data/Human.miRNA.fa 20

FastaSeqLengthFilterLower.py data/Human.miRNA.fa 18

FastaSeqLinearizer.py data/Human.miRNA.fa

FastaSeqNucleotideCounter_ATCG.py data/Human.miRNA.fa data/output.txt

FastaSeqORFShifter.py data/Human.miRNA.fa
