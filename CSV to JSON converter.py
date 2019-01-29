'''
This application will:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object.

# - store the JSON object into json_file.txt
'''

import json

with open('csv_file.txt', 'r') as cf:
    club_list = [each_line.strip() for each_line in cf.readlines()]

json_list = []
for each_club in club_list:
    club, city, country = each_club.split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

with open('jason_file.txt', 'w') as jf:
    json.dump(json_list, jf)

