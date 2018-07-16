__author__ = 'amoriarty'
import requests
import csv
import json
url = "https://api.thomsonreuters.com/permid/calais"

#The Imput file should be the brief description of the objects - this is the data that is run against the API.

f=open("Input.csv","rb")
r=open("Output.csv","ab")
rr=csv.writer(r)
h=csv.reader(f)

for row in h:
    try:
        row=str(row)
        row=row.encode('utf-8')
        payload = row
        headers = {
            'content-type': "text/raw",
            'accept': "application/json",
            'x-ag-access-token': "YOUR KEY",
            'x-calais-language': "English",
            'outputformat': "application/json",
            'cache-control': "no-cache",
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        parsed_json = json.loads(response.text)
        docID=parsed_json['doc']['info']['docId']
        docID = str(docID)
        tag1= parsed_json [docID+ "/SocialTag/1"]["name"]
        tag2= parsed_json [docID+ "/SocialTag/2"]["name"]
        tag3= parsed_json [docID + "/SocialTag/3"]["name"]
        tag4= parsed_json [docID + "/SocialTag/4"]["name"]
        mydata=[[row,tag1,tag2,tag3,tag4]]
        rr.writerows(mydata)

    except KeyError:
        mydata = [[row,"Key Error"]]
        rr.writerows(mydata)
    except AttributeError:
        mydata = [[row,"Attribute Error"]]
        rr.writerows(mydata)
    except UnicodeEncodeError:
        mydata = [[row,"Unicode Error"]]
        rr.writerows(mydata)
    except ValueError:
        mydata = [[row,"Value Error"]]
        rr.writerows(mydata)
