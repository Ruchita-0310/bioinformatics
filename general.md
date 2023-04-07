# ARC
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
scp -i .ssh/ccc_cloud_ghost -o UserKnownHostsFile=/dev/null  arch@206.12.90.119:/bio/data/Ruchita/file_name ~/Downloads # download files from ARC to mac
```
# Blast
## merging files/concatanating flies
```
cat file_name.1 file_name.2 file_name.3 > new_file_name 
makeblastdb -in new_file_name -dbtype prot # making blast database for protein sequence
blastp -db new_file_name -query new_file_name -out blast_file_name.out -outfmt 6 #blast experiment with options
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

# usearch clustering
```
/bio/bin/usearch -cluster_fasta new_file_name -id 0.9 centeroids usearch_file_name.faa
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
rm -d dir_name #empty directory
rm -r dir_name #non-empty dirctory and its content
```

# List
```
ls # list all the files in the current directory
ls -lrt # list with ownership - read/write/view...
ls -al # hidden files
```

# Move and/or rename
```
mv ./current_path/file1 ./destination_path/file1
```

# Move from one directory to another
```
cd .. # moves to previous directory
cd ../.. # moves to 2 previous directory
cd directoryB # moves to another directory called directoryB
cd ../directoryC # will go back to the parent directory and then go to directoryC
```

# Word count
```
ls -1 *.ale | wc -l # for .ale file # could be any file
```
