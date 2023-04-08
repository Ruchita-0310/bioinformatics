# 1. Activate python and other pathways
```
source /bio/bin/python-env/bin/activate
source /bio/bin/profile
```
# 2. Cloning Dr. Marc Strous's page
```
git clone https://github.com/kinestetika/ComparativeGenomics.git
cd ComparativeGenomics/
python -m build
pip install --upgrade dist/comparative_genomics-0.1.tar.gz
```
# 3. Orthologous
- The "orthologues" software is designed to identify orthologous genes between different organisms or sequences, and to cluster them into groups of orthologous gene families.
- Make an output directory for orthologs 
```
mkdir /bio/data/Ruchita/phormidium/output 
```
- Orthologs command line (remove all the non .faa files)
```
orthologues --input_dir /bio/data/Ruchita/phormidium --output_dir /bio/data/Ruchita/phormidium/output 
```
# 4. tree_of_mags
- The Tree of MAGs is important for several reasons:
 1. it provides a way to study the diversity of microbial communities and their evolutionary relationships. This can help researchers understand how different microbial communities are related to one another, and how they have evolved over time.
 2. the Tree of MAGs can be used to identify new microbial lineages that have not been previously described. By comparing MAGs from different samples, researchers can identify novel clades of microorganisms that may have important ecological or biotechnological implications.
 3. the Tree of MAGs can be used to study the functional capabilities of microbial communities. By examining the presence or absence of specific genes or pathways across the phylogenetic tree, researchers can infer the functional capabilities of different microbial clades. This can help identify novel enzymes or pathways that may have biotechnological applications, such as in the production of biofuels or other bioproducts.
```
tree_of_mags –dir input_directory
```
# 5. FastTree
- FastTree is a bioinformatics software tool that is commonly used for the phylogenetic analysis of DNA and protein sequences. Its main function is to construct phylogenetic trees quickly and accurately from a large number of sequences.
```
FastTree input_dir/file.name > fasttree_file
```
# 6. Metaerg 
- Metaerg is an important tool for metagenomic analysis because it allows researchers to accurately and comprehensively analyze the functional potential of complex microbial communities, and to generate insights into their roles in a wide range of biological processes.
```
/bio/bin/python-env/bin/metaerg --contig_file /bio/data/directory/file_name --database_dir /bio/databases/metaerg 
```
- **Results**: it will produce .xls file which can be downloaded on the computer and viewed it in excel
# 7. Installing CheckM2
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
8. Checkm2 command: [OPTIONS]
`-t 30`: specifies the number of CPU threads to use for the computation (in this case, 30 threads).
`-x fna`: specifies the input file format as FNA.
`--input {input_directory_name.fna}`: specifies the directory containing the input files to analyze.
`--output-directory {output_directory_name}`: specifies the name of the output directory where the results will be saved.
```
checkm2 predict -t 30 -x fna --input ./directory_name.fna --output-directory output_directory_name
```
# 8. IQ Tree
- IQ-TREE supports a wide range of evolutionary models
- All common substitution models for DNA, protein, codon, binary and morphological data with rate heterogeneity among sites
## 8.1. iqtree2 - species tree
- Use `concatenated_alignment` file 
- View the tree in different tree viewing programs (iTOL, RaXml, FigTree, Fasttree...)
- In this case, iTOL was used. iTOL produces unrooted tree, and it can be rerooted at different branches in the tree. 3 different rerooted tree data were used to run ALE observe. 
```
nohup iqtree2 -s /bio/data/Ruchita/faa/alignments/concatenated_alignment
```
## 8.2. iqtree2 – gene tree | run it in loop
```
nohup sh -c 'for file in /bio/data/Ruchita/faa/orthologous/msa_clustalo/*aln; do iqtree2 -s "$file" -m MFP -madd LG+C20,LG+C60 -B 10000 -wbtl ; done' &
```
# 9. ClustalO multiple sequence alignment (MSA) | run it in loop 
- ClustalO is a software tool used for multiple sequence alignment. It is designed to align three or more nucleotide or amino acid sequences, based on their similarity. The main purpose of ClustalO is to identify regions of similarity between the sequences, and to produce a multiple sequence alignment that maximizes the overall similarity.
- ClustalO will use .faa files that are produced after running orthologues command.
```
for file in /bio/data/Ruchita/faa/orthologous/*.faa; do nohup clustalo -i "$file" -o /bio/data/Ruchita/faa/orthologous/msa_clustalo"$(basename "$file" .faa)".aln > "$(basename "$file" .faa)".log & done
```
- **Results**: 
1. 18 genes are not aligned because there is only 1 sequence
2. The command will produce .aln.ufboot files
# 10. ALE observe | run it in loop
- ALE (Assembly Likelihood Estimator) Observe is a software tool used in genome assembly evaluation. It is designed to compare an assembled genome to a reference genome to determine the accuracy of the assembly.
- The tool does this by calculating the likelihood that each read in the assembly could have come from the reference genome. A high likelihood suggests that the read is likely to be correct, while a low likelihood suggests that the read may be misassembled or contain errors.
- ALE Observe can be used to identify regions of the assembly that are likely to be correct, as well as regions that may contain errors or require further investigation. This information can be used to improve the quality of the assembly or identify potential areas of interest for further research.
```
nohup sh -c 'for file in /bio/data/Ruchita/ale1 /*.ufboot; do ALEobserve $file; done' &
```
- **Results**: 
1. The command will produce .ale files
## 10.1. ALE_undated | run it in parallel or loop
- ALE_undated provides a quantitative measure of assembly accuracy that can help researchers assess the quality of their genome assembly and guide future research efforts. It is particularly useful when comparing genomes from different lineages where the timing of divergence is not well-known.
- Use the .ale files produced in the previous step to run this command
```
parallel -j 100000 "ALEml_undated reroot_newick.txt {} separators='|'" ::: *.ale
nohup parallel -j 1500 “ALEml_undated reroot_newick.txt {} separators='|'" ::: *.ale &
```
- You can adjust the number of parallel jobs by adding the "-j" flag followed by the number of parallel jobs you want to run
- **Results**:
1. The command will produce .uml_rec and .ale.uTs files
2. Use only .uml_rec files!
## 10.2. Likelihood table
1. Move all the .ale.uml_rec files to reroot1, reroot2 and reroot3 directories respectively
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
- **Results**: 
1. Use `au_test_out` to figure out the p-vales of the rerooted trees and use the tree that has p-value 1.00
2. From the table, it was inferred that reroot2 was the best (further used in 10.4).
## 10.3. Robustness check
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
python DTL_ratio_analysis_ML_diff.py reroot2 LS # use the reroot tree that has a p-value of 1.00 (in this case it is reroot2)
```
- **Results**:
1. `LS_ratio_results` directory has the results
2. Produced multiple .png files that contain graphs and .csv files that has tables.
```
zip ls.zip LS_ratio_results/*
```
- Downloaded the zipped file on the computer to view
## 10.4. Gene content evolution on the most likely rooted species tree | run it in "reroot2" directory
### 10.4.1. Branchwise events
- Once the most likely root has been identified, this technique allows users to quantify the relative contributions of duplication, transfer, loss, and origination in the gene content evolution
- copy [branchwise_number_of_events.py](https://github.com/ak-andromeda/ALE_methods/blob/main/branchwise_number_of_events.py)
```
python branchwise_number_of_events.py > dtloc.tsv # run this command in reroot2 directory only!
```
- **Results**:
1. Now open .tsv file that contains a table (use 16 and 30 as internal nodes). 
2. Internal nodes play a critical role in gene content evolution analyses as they represent the points in the phylogenetic tree where gene gain and loss events are inferred to have occurred, and provide insights into the evolutionary history of the gene.
### 10.4.2. Ancestral reconstruction
- Copy [Ancestral_reconstruction_copy_number.py](https://github.com/ak-andromeda/ALE_methods/blob/main/Ancestral_reconstruction_copy_number.py)
```
nano Ancestral_reconstruction_copy_number.py # change .ml_rec to .uml_rec
```
- The ALE output also provides estimates of the gene families present at each node. Therefore we can model the presence and absence of gene families at internal nodes, reconstructing ancestral genomes
- There are three command line arguments. The first is the minimum copy number at which a gene family should be included in the reconstruction , i.e., 0.5 = on average, half a copy of the family is present at the node in question (fractions are possible because the value is averaged over the sampled reconciliations)
- The secondnd third arguments are the range of the internal nodes. For example, in this dataset the internal nodes are labelled 16, 17, 18... 30 (as can be seen in the output of branchwise_number_of_events.py). Thus, the command line arguments are 16 and 30. All nodes between 16 and 30 will be reconstructed
```
python Ancestral_reconstruction_copy_number.py 0.5 16 30
```
- **Results**: `Total_copies_at_node` and `Gene_families_at_each_node` directories will contain .csv files
- Zip it and download it to your computer to view
