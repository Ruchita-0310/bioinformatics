source /bio/bin/profile #activates programs not in python env
source /bio/bin/python-env/bin/activate #activate programs in python env

sudo mkdir /bio/data/Ruchita #making directory
sudo chown arch Ruchita #changing directory

#macOS file transfer
scp -i .ssh/ccc_cloud_ghost -o UserKnownHostsFile=/dev/null ~/Downloads/file_name.faa arch@206.12.90.119:/bio/data/Ruchita 

cat file_name.1 file_name.2 file_name.3 > new_file_name #concatanating flies

makeblastdb -in new_file_name -dbtype prot # making blast database for protein sequence

blastp -db new_file_name -query new_file_name -out blast_file_name.out -outfmt 6 #blast experiment with options

#MCL blast
cut -f 1,2,11 seq.cblast > seq.abc
mcxload -abc seq.abc --stream-mirror --stream-neg-log10 -stream-tf 'ceil(200)' -o seq.mci -write-tab seq.tabmcl seq.mci -I 1.4
mcl seq.mci -I 2
mcl seq.mci -I 4
mcl seq.mci -I 6
mcxdump -icl out.seq.mci.I14 -o dump.seq.mci.I14 -tabr seq.dict
mcxdump -icl out.seq.mci.I20 -o dump.seq.mci.I20 -tabr seq.dict
mcxdump -icl out.seq.mci.I40 -o dump.seq.mci.I40 -tabr seq.dict
mcxdump -icl out.seq.mci.I60 -o dump.seq.mci.I60 -tabr seq.dict

#usearch clustering
/bio/bin/usearch -cluster_fasta new_file_name -id 0.9 centeroids usearch_file_name.faa

#prodigal
prodigal -i file.fna -o new_file.faa
prodigal - i file.fna -a protein.faa -o genes.gbk

#unzip
unzip file_name.zip

#remove a file
rm file_name

#remove directory
rm -d dir_name #empty directory
rm -r dir_name #non-empty dirctory and its content

#list
ls
ls -lrt #list with ownership - read/write/view...

#move and/or rename
mv ./current_path/file1 ./destination_path/file1

#move from one directory to another
cd .. (moves to previous directory)
cd ../.. (moves to 2 previous directory)

# Word count
ls -1 *.ale | wc -l # for .ale file (could be any file)