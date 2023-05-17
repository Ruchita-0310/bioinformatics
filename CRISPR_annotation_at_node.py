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
            
lookup_data = []

for gene_family in gene_families:
    lookup_data.append(gene_family)
    # Open the CSV file containing the data to be looked up in read mode
    if os.path.exists('orth_out/'+gene_family[2].split('clustalo')[1].split(".aln")[0] + '.faa'):
        with open('orth_out/'+gene_family[2].split('clustalo')[1].split(".aln")[0] + '.faa', mode='r') as data_file:
            data_reader = data_file.read()

            # Filter out annotations that don't contain 'CRISPR' and 'toxin'.
            if 'CRISPR' not in data_reader and 'toxin' not in data_reader:
                lookup_data.remove(gene_family)
                continue
            sequences = data_reader.split('>')

            # Iterate over each sequence.
            for sequence in sequences:
                # Filter out 'Paralogue' sequences.
                if '#' not in sequence and sequence != "" and '[Paralogue]' not in sequence:
                    # 'GeitlerinemaP-1104|3716 [Orthologue] GeitlerinemaP-1104|GeitlerinemaP-1104.NZ_SMDP01000009.1.00478 type II toxin-antitoxin system VapC family toxin (Bacteria; Cyanobacteria; Cyanobacteriia; Cyanobacteriales; Geitlerinemaceae; Phormidium_A; Phormidium_A)'
                    first = sequence.split(';')
                    bacteria = first[len(first)-1].split(')')[0]
                    annotation = sequence.split('(')[0].split('|')[2]
                    if len(annotation.split(' ')) == 1:
                        continue
                    annotation = annotation.split(' ', 1)[1]
                    annotation = ['', '', '', '', '', '', '', '', bacteria, annotation]
                    lookup_data.append(annotation)

                # if annotation does not exists, only print bacteria.
                if '#' in sequence:
                    bacteria = sequence.split('|')[0]
                    annotation = ['', '', '', '', '', '', '', '', bacteria, '']
                    lookup_data.append(annotation)

# Create a new file in write mode
with open('CRISPR_annotation_at_node.csv', mode='w', newline='') as keys_file:
    # Create a CSV writer object and set the delimiter to tabs
    keys_writer = csv.writer(keys_file, delimiter=',')

    # Add column names
    value = ['', 'Node', 'Gene_family', 'Duplications', 'Transfers', 'Losses', 'Originations', 'Copies', 'Probable bacteria', 'Probable protein annotation']
    keys_writer.writerow(value)

    # Iterate over the lookup keys and perform a lookup in the data dictionary
    for row in lookup_data:
        # Write a new row to the keys file with the key and the lookup value
        keys_writer.writerow(row)
