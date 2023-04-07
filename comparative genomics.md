# Activate python and other pathways
```
source /bio/bin/python-env/bin/activate
source /bio/bin/profile
```
# Cloning Marc's page
```
git clone https://github.com/kinestetika/ComparativeGenomics.git
cd ComparativeGenomics/
python -m build
pip install --upgrade dist/comparative_genomics-0.1.tar.gz
```

# Orthologous
- output directory for orthologs 
```
mkdir /bio/data/Ruchita/phormidium/output 
```
- orthologs command line (remove all the non .faa files)
```
orthologues --input_dir /bio/data/Ruchita/phormidium --output_dir /bio/data/Ruchita/phormidium/output 
```

# tree_of_mags
```
tree_of_mags –dir input directory
```

# FastTree
```
FastTree inputdir/file.name > fasttree_file
```

# Metaerg 
```
/bio/bin/python-env/bin/metaerg --contig_file /bio/data/Ruchita/cyano-fna --database_dir /bio/databases/metaerg 
```

# Installing CheckM2
1.	Install [python 3.8](https://aur.archlinux.org/packages/python38):
```
cd /bio/bin
git clone https://aur.archlinux.org/python38.git
cd python38
makepkg
```

2. Installing virtual env:
```
pip install virtualenv
```

3. Installing checkm2 in the virtualenv: 
```
virtualenv --python=/bio/bin/python38/pkg/python38/usr/bin/python3.8 checkm2
```

4. Update library path:
```
export LD_LIBRARY_PATH=/bio/bin/lib:/bio/bin/python38/pkg/python38/usr/lib
```

5. Activating checkm2 pathway:
```
source /bio/bin/checkm2/bin/activate
```

6. installing checkm2:
```
pip install checkm2
```

7. Download checkm2 database:
```
checkm2 database –download
```

8. Checkm2 command:
```
checkm2 predict -t 30 -x fna --input ./directory_name.fna --output-directory output_directory_name
```

# iqtree2 - species tree
```
nohup iqtree2 -s /bio/data/Ruchita/faa/alignments/concatenated_alignment
```
IQ-TREE supports a wide range of evolutionary models
All common substitution models for DNA, protein, codon, binary and morphological data with rate heterogeneity among sites.

# iqtree2 – gene tree | run it in loop
```
nohup sh -c 'for file in /bio/data/Ruchita/faa/orthologous/msa_clustalo/*aln; do iqtree2 -s "$file" -m MFP -madd LG+C20,LG+C60 -B 10000 -wbtl ; done' &
```

# Clustalo (MSA)multiple sequence alignment | run it in loop 
```
for file in /bio/data/Ruchita/faa/orthologous/*.faa; do nohup clustalo -i "$file" -o /bio/data/Ruchita/faa/orthologous/msa_clustalo"$(basename "$file" .faa)".aln > "$(basename "$file" .faa)".log & done
```

# ALE observe | run it in loop
```
nohup sh -c 'for file in /bio/data/Ruchita/ale1 /*.ufboot; do ALEobserve $file; done' &
```

# ALE_undated | run it in parallel or loop
```
parallel -j 100000 "ALEml_undated reroot_newick.txt {} separators='|'" ::: *.ale
nohup parallel -j 1500 “ALEml_undated reroot_newick.txt {} separators='|'" ::: *.ale &
```
- You can adjust the number of parallel jobs by adding the "-j" flag followed by the number of parallel jobs you want to run

# Likelihood table
1. Move all the .ale.uml_rec to reroot1, reroot2 and reroot3 directories respectively
2. rename all reroot_newick2.uml_rec and reroot_newick3.uml_rec to reroot_newick
3. copy [write_consel_file.py3](https://github.com/ak-andromeda/ALE_methods/blob/main/write_consel_file_p3.py) 

```
rename reroot_newick2 reroot_newick * 
nano write_consel_file.py 
python write_consel_file.py reroot1 reroot2 reroot3 > likelihoods_table 
makermt likelihoods_table.mt
consel likelihoods_table
/bio/bin/consel/bin/catpv likelihoods_table > au_test_out
```

# Robustness check
- copy [DTL_ratio_analysis_ML_diff.py](https://github.com/ak-andromeda/ALE_methods/blob/main/write_consel_file_p3.py)
- make: roots_to_test.txt 
```
nano DTL_ratio_analysis_ML_diff.py
nano roots_to_test.txt
```

roots_to_test.txt
```
reroot1
reroot2
reroot3
```

make: species_list_demo.txt
```
nano species_list_demo.txt
```

species_list_demo.txt
```
cyanoSBC 
gBBD               
GeitlerinemaPCC_9228 
gFC2
MicrocoleusPCC_7113 
pha
pSHIP  
cyanoSID2
placuna 
pwillei
Sodalinemagerasimenkoae
Baaleninemasimplex     
GeitlerinemaP-1104
pBIN05 
pOSCR
pyuhuli
```

```
mkdir reroot
cp -r reroot1 reroot
cp -r reroot2 reroot
cp -r reroot3 reroot
python DTL_ratio_analysis_ML_diff.py reroot LS
```
Results were stored in `LS_ratio_results` directory
```
zip ls.zip LS_ratio_results/*
```
