__author__ = 'Moriarty'
import requests
import csv
import json
f=open("c.csv","rb")

# The CSV should contain Auckland Museum API image links without the rending information
#eg. http://api.aucklandmuseum.com/id/media/v/320810

r=open("brokenlink.csv","ab")
rr=csv.writer(r)
h=csv.reader(f)

for row in h:
    row = ''.join(row)
    row = row +str("/metadata")
    print (row)
    try:
        headers = {
         'accept': "application/json"
         }

        response = requests.request("GET", row, headers=headers)
        #print(response)
        parsed_json = json.loads(response.text)
        image = parsed_json ["am:filesize"]
        #print(image)

    except ValueError:  # includes simplejson.decoder.JSONDecodeError

        res=[''.join(row),response]
        rr.writerow(res)
f.close()
r.close()
