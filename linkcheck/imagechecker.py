__author__ = 'Moriarty'
import requests
import csv
import json

# list.csv should contain Auckland Museum API image links without rendering information
# e.g. http://api.aucklandmuseum.com/id/media/v/320810

with open('List2.csv', "r") as list:
    l = csv.reader(list)
    for row in l:
        row = ''.join(row)+str("/metadata")

        # set headers, otherwise API sends image
        headers = {'accept': "application/json"}
        response = requests.get(row, headers=headers)

        if response.status_code == 404:
            with open("errorsTEST.csv","ab") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([row])
            print "Added 1."

list.close()
