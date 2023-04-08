# Cloud server
- making directory
```
sudo mkdir /bio/data/Ruchita
```
- changing directory
```
sudo chown arch Ruchita
```

# macOS file transfer
```
scp -i .ssh/ccc_cloud_ghost -o UserKnownHostsFile=/dev/null ~/Downloads/file_name.faa arch@206.12.90.119:/bio/data/Ruchita # upload files from mac to ARC
scp -i .ssh/ccc_cloud_ghost -o UserKnownHostsFile=/dev/null  arch@206.12.90.119:/bio/data/Ruchita/file_name ~/Downloads    # download files from ARC to mac
```
# Unzip
```
unzip file_name.zip
```

# Remove 
```
rm file_name # will remove a file
```

## Remove directory
```
rm -d dir_name # empty directory
rm -r dir_name # non-empty dirctory and its content
```

# List
```
ls      # list all the files in the current directory
ls -lrt # list with ownership - read/write/view...
ls -al  # hidden files
```

# Move and/or rename
```
mv ./current_path/file1 ./destination_path/file1
```

# Move from one directory to another
```
cd ..            # moves to previous directory
cd ../..         # moves to 2 previous directory
cd directoryB    # moves to another directory called directoryB
cd ../directoryC # will go back to the parent directory and then go to directoryC
```

# Word count
```
ls -1 *.ale | wc -l # for .ale file # could be any file
```

# Resource Monitor
```
top
```

# Find text in file
```
grep "pattern" filename.txt
```

# Download files
```
wget link_to_file
wget -O newfilename.txt http://example.com/file.txt # Download a file and save it with a different name
wget -i url_list.txt                                # Download multiple files from a URL list
```

# Blast
- There are different types of BLAST options available
1. `BLASTP` - This command is used to search for protein sequences that match a given protein sequence in a protein database.
2. `BLASTN` - This command is used to search for nucleotide sequences that match a given nucleotide sequence in a nucleotide database.
3. `BLASTX` - This command is used to search for protein sequences that match a given nucleotide sequence in a nucleotide database. This type of BLAST compares the six-frame translations of the nucleotide sequence to a protein database.
- There are different output formats 
- `-outfmt 6` specifies a tabular format that includes the following columns:
1. Query ID
2. Subject ID
3. Percent identity
4. Alignment length
5. Mismatches
6. Gap openings
7. Query start
8. Query end
9. Subject start
10. Subject end
11. E-value
12. Bit score
- Other formats include
1. `-outfmt 0` (Pairwise): This format is similar to the default output format, but it's designed to be more easily parsed by computer programs. Each match between a query sequence and a subject sequence is reported as a separate block of text with labels for each section of the output.
2. `-outfmt 5` (XML): This format produces output in XML format, which can be useful for further processing and analysis using computer programs.
3. `-outfmt 7` (Text ASN.1): This format is similar to the default output format, but it uses ASN.1 (Abstract Syntax Notation One) encoding to represent the results. It's primarily used for database submissions.
4. `-outfmt 10` (Comma-separated values): This format produces a CSV file with comma-separated values for each of the columns in the output.
5. `-outfmt 11` (Binary ASN.1): This format is similar to -outfmt 7, but it uses a binary encoding instead of text encoding, which can make it faster and more compact for very large datasets.
6. `-outfmt 15` (JSON): This format produces output in JSON format, which can be useful for further processing and analysis using computer programs.
```
blastp -db new_file_name -query new_file_name -out blast_file_name.out -outfmt 6 
```
## Making blast database for protein sequences
```
makeblastdb -in new_file_name -dbtype prot
```
## Merging files/concatanating flies
```
cat file_name.1 file_name.2 file_name.3 > new_file_name 
```

## MCL blast
- MCL Blast is commonly used in genome annotation, comparative genomics, and protein structure prediction. It can help identify gene families, functional domains, and conserved motifs in protein sequences. MCL Blast can also be used to identify evolutionary relationships between different species based on their genetic sequences. Overall, the purpose of running MCL Blast is to help researchers gain a deeper understanding of the relationships between genes and proteins, which can ultimately lead to new insights and discoveries in biology and medicine.
```
cut -f 1,2,11 seq.cblast > seq.abc
mcxload -abc seq.abc --stream-mirror --stream-neg-log10 -stream-tf 'ceil(200)' -o seq.mci -write-tab seq.tabmcl seq.mci -I 1.4
mcl seq.mci -I 2
mcl seq.mci -I 4
mcl seq.mci -I 6
mcxdump -icl out.seq.mci.I14 -o dump.seq.mci.I14 -tabr seq.dict
mcxdump -icl out.seq.mci.I20 -o dump.seq.mci.I20 -tabr seq.dict
mcxdump -icl out.seq.mci.I40 -o dump.seq.mci.I40 -tabr seq.dict
mcxdump -icl out.seq.mci.I60 -o dump.seq.mci.I60 -tabr seq.dict
```

# USEARCH clustering
- USEARCH is a bioinformatics tool that provides a fast and efficient method for clustering nucleotide or protein sequences. Clustering is a common step in bioinformatics pipelines that groups similar sequences together based on a pre-defined similarity threshold.
- In USEARCH, clustering is performed using the cluster command. The tool takes a set of input sequences and groups them into clusters based on pairwise sequence similarity. The user specifies a similarity threshold (usually a percentage identity or an E-value cutoff) that defines the maximum allowed difference between two sequences to be considered part of the same cluster.
- The `cluster_fast` algorithm to cluster the sequences in the input.fasta file. 
- The `-id` option specifies the similarity threshold for clustering (in this case, 0.9)
- The `-centroids` option specifies the output file for the representative sequences in each cluster 
```
/bio/bin/usearch -cluster_fast file_name.faa -id 0.9 centeroids usearch_file_name.faa
```

# Prodigal 
- Prodigal is a bioinformatics tool used for gene prediction or gene finding in microbial genomes. It is a fast and efficient gene prediction program that is widely used in genome annotation projects. Prodigal uses a combination of hidden Markov models (HMMs) and a dynamic programming algorithm to identify open reading frames (ORFs) in genomic sequences.
- `-i` input_file
- `-o` output_file
- `-a` generate a FASTA-formatted file containing the amino acid sequences of the predicted protein-coding genes in the input genome
```
prodigal -i file.fna -o new_file.faa
prodigal - i file.fna -a protein.faa -o genes.gbk
```
