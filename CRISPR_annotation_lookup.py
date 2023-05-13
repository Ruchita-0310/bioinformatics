import csv
import os

# Create an empty list to store the lookup keys
gene_families = []

# Open the CSV file containing the lookup keys in read mode
with open('Copies_at_each_node.csv', mode='r') as keys_file:
    # Create a CSV reader object and set the delimiter to tabs
    keys_reader = csv.reader(keys_file, delimiter=',')

    # Iterate over each row in the keys file and add the keys to the list
    for row in keys_reader:
        if row[2] != "Gene_family":
            gene_families.append(row)
        else:
            print(row)
            #	Node	Gene_family	Duplications	Transfers	Losses	Originations	Copies	 

lookup_data = []

for gene_family in gene_families:
    lookup_data.append(gene_family)
    #print(gene_family)
    if os.path.exists('ortho_output/'+gene_family[2].split('.txt_')[1].split(".aln")[0] + '.faa'):
        # Open the CSV file containing the data to be looked up in read mode
        with open('ortho_output/'+gene_family[2].split('.txt_')[1].split(".aln")[0] + '.faa', mode='r') as data_file:
            # Create a CSV reader object and set the delimiter to tabs
            data_reader = data_file.read()
            if 'CRISPR' not in data_reader and 'toxin' not in data_reader:
                lookup_data.remove(gene_family)
                continue
            sequences = data_reader.split('>')

            # Iterate over each row in the data file
            for sequence in sequences:
                if '#' not in sequence and sequence != "" and '[Paralogue]' not in sequence:
                    #print(sequence)
                    #sequence = 'GeitlerinemaP-1104|5166 [Orthologue] GeitlerinemaP-1104|WP_170189656.1 helicase [Geitlerinema sp. P-1104]'
                    first = sequence.split('[')
                    x = first[len(first)-1].split(']')[0]
                    #print(x)
                    y = sequence.split('[' + x)[0].split('.')[1]
                    #print(y)
                    y = y.split(' ', 1)[1]
                    #print(y)
                    a = ['', '', '', '', '', '', '', '', x, y]
                    lookup_data.append(a)
                    #print(a)
                if '#' in sequence:
                    x = sequence.split('|')[0]
                    a = ['', '', '', '', '', '', '', '', x, '']
                    lookup_data.append(a)
                    #print(a)
    #print(lookup_data)
    #break

# Open the keys file again, this time in write mode
with open('CRISPR_annotation_at_node_lookup.csv', mode='w', newline='') as keys_file:
    # Create a CSV writer object and set the delimiter to tabs
    keys_writer = csv.writer(keys_file, delimiter=',')

    # Add column names
    value = ['', 'Node', 'Gene_family', 'Duplications', 'Transfers', 'Losses', 'Originations', 'Copies', 'Probable bacteria', 'Probable protein annotation']
    keys_writer.writerow(value)

    # Iterate over the lookup keys and perform a lookup in the data dictionary
    for row in lookup_data:
        # Write a new row to the keys file with the key and the lookup value
        keys_writer.writerow(row)
