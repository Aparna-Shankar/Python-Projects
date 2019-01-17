
""" Read and parse a CSV file """

import csv

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

# with open('new_names.csv', 'w') as csv_copy:
#     csv_writer = csv.writer(csv_copy, delimiter='\t')

#     for line in csv_reader:
#         csv_writer.writerow(line)
# --------------------------------------------------------------------------------------------------

# Using DictReader & Dictwriter instead of the regular reader & writer
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)

    with open('new_names.csv', 'w') as csv_copy:

        fieldnames = ['first_name', 'last_name']  # Define the field names

        csv_writer = csv.DictWriter(csv_copy, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()  # Write the header first

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
