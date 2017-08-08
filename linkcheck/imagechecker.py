__author__ = 'Moriarty'
import requests
import csv
import json

# list.csv should contain Auckland Museum API image links without rendering information
# e.g. http://api.aucklandmuseum.com/id/media/v/320810

with open('list.csv', "r") as list:
    l = csv.reader(list)
    for row in l:
        row = ''.join(row)
        row = row+str("/metadata")
        headers = {'accept': "application/json"}
        response = requests.request("GET", row, headers=headers)
        res = [''.join(row),response]
        if "404" in str(res):
            with open("errors.csv","ab") as outfile:
                writer = csv.writer(outfile)
                writer.writerow(res)


list.close()
