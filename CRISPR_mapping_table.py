import csv
import os

keys = []
all_rows = {}
with open('blastp_results.csv', mode='r') as keys_file:
    # Create a CSV reader object and set the delimiter to tabs
    keys_reader = csv.reader(keys_file, delimiter=',')

    # Iterate over each row in the keys file and add the keys to the list
    for row in keys_reader:
        if 'subject ID' not in row[1] and row[1] not in keys:
            keys.append(row[1])
            all_rows[row[1]] = row

sequences = {}

# Open the CSV file containing the lookup keys in read mode
with open('concat.faa', mode='r') as data_file:
    # Create a CSV reader object and set the delimiter to tabs
    data_reader = data_file.read().split('>')
    for data in data_reader:
        s = data.split(')')[0]
        x = s.split(' ')[0]
        if x == "":
            continue
        y = s.split(x)[1] + ')'
        sequences[x] = y



# Open the keys file again, this time in write mode
with open('CRISPR_mapping_table.csv', mode='w', newline='') as keys_file:
    # Create a CSV writer object and set the delimiter to tabs
    keys_writer = csv.writer(keys_file, delimiter=',')

    # Add column names
    value = ['query ID', 'subject ID', 'identity', 'alignment length', 'mismatches', 'gap opening', 'query start', 'query end', 'subject start', 'subject end', 'e-value', 'bit score', 'annotation']
    keys_writer.writerow(value)

    for key in keys:
        print(key)
        value = all_rows[key]
        search = key#.split('.')[1] + '.' + key.split('.')[2] + 
        if search in sequences and ('CRISPR' in sequences[search] or 'RAMP' in sequences[search]):
            value.append(sequences[search])
        else:
            value.append("")
        keys_writer.writerow(value)
