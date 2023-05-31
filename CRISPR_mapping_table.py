import csv
import os

keys = []
all_rows = {}
with open('blastp_results.csv', mode='r') as keys_file:
    # Create a CSV reader object and set the delimiter to tabs
    keys_reader = csv.reader(keys_file, delimiter=',')

    # Iterate over each row in the keys file and add the keys to the list
    for row in keys_reader:
        if 'subject ID' not in row[1] and row[1] not in keys and row[2] == '100':
            keys.append(row[1])
            all_rows[row[1]] = row

# This will store the annotation against the subject ID as key
sequences = {}

# This will store the fasta file numbers against the subject ID as key
file_names = {}

for file in os.scandir('orth_out'):
    # Open the CSV file containing the lookup keys in read mode
    with open('orth_out/' + file.name, mode='r') as data_file:
        # Create a CSV reader object and set the delimiter to tabs
        data_reader = data_file.read().split('>')
        for data in data_reader:
            # Ignore everything that is not orthologue 
            if 'Orthologue' not in data:
                continue
            # Extract subject ID
            s = data.split('|')[2]
            x = s.split(' ')[0]
            if x == "":
                continue
            # Extract annotations
            y = s.split(x)[1].split('(')[0]
            sequences[x] = y
            file_names[x] = file.name 

# Create a new file in write mode
with open('CRISPR_mapping_table.csv', mode='w', newline='') as keys_file:
    # Create a CSV writer object and set the delimiter to tabs
    keys_writer = csv.writer(keys_file, delimiter=',')

    # Add column names
    value = ['query ID', 'subject ID', 'identity', 'alignment length', 'mismatches', 'gap opening', 'query start', 'query end', 'subject start', 'subject end', 'e-value', 'bit score', 'annotation', 'fasta_file']
    keys_writer.writerow(value)

    for key in keys:
        value = all_rows[key]
        search = key
        # If subject ID has annotation and if annotation has CRISPR or RAMP, it shall print
        if search in sequences and ('CRISPR' in sequences[search] or 'RAMP' in sequences[search]):
            value.append(sequences[search])
            value.append(file_names[search])
        else:
            value.append("")
            value.append("")
        keys_writer.writerow(value)

        
