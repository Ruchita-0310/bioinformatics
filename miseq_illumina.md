# run zipped file on Metaamp 
- results will be multiple folder
- open "otu_and_taxonomy"
- run blastn on "MiSeqall.otu.fasta" 
```
blastn -db /bio/databases/metaerg/db_rna.fna -query MiSeqall.otu.fasta -max_target_seqs 1 -outfmt 6 
```
- results interpretation (it will be in a table format)
1. query_id: the identifier of the query sequence
2. subject_id: the identifier of the matching subject sequence
For example: `p~22609~1527~lcl|NZ_CP054306.1_rrna_28~~1489~27 is the subject ID`
    *	p: This letter may indicate the type of sequence, in this case perhaps "protein".
    *	22609: This may be an internal database identifier, which is not meaningful outside the specific database and its indexing scheme.
    *	1527: This may be another internal identifier or a reference to the sequence position within the database, but its meaning is again dependent on the database and indexing scheme used.
    *	lcl|NZ_CP054306.1_rrna_28: This is the sequence identifier for the matching subject sequence in the NCBI nucleotide database (nt), specifically for the genome assembly with accession number NZ_CP054306.1. The lcl prefix may indicate that this is a local sequence identifier, rather than a stable accession number. The rest of the string rrna_28 likely refers to the type of sequence (ribosomal RNA, in this case the 28S subunit).
    *	~: This tilde separates the previous information from the following information.
    *	~1489: This could represent the length of the subject sequence that was matched by the query sequence.
    *	~27: This could represent the alignment score of the match, such as the bit score or some other score.
3. % identity: the percentage identity between the query and subject sequences 
4. alignment_length: the length of the alignment between the query and subject sequences
5. mismatches: the number of mismatches in the alignment
6. gap_opens: the number of gaps (insertions or deletions) in the alignment
7. q_start: the starting position of the alignment in the query sequence
8. q_end: the ending position of the alignment in the query sequence
9. s_start: the starting position of the alignment in the subject sequence
10. s_end: the ending position of the alignment in the subject sequence
11. evalue: the E-value of the match, representing the expected number of matches by chance
12. bit_score: the bit score of the match, representing the strength of the match

