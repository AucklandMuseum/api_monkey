__author__ = 'amoriarty'
import requests
import csv
import json
url = "https://api.thomsonreuters.com/permid/calais"

f=open("aad.csv","rb")
r=open("OpenCaltest.csv","ab")
rr=csv.writer(r)
h=csv.reader(f)

for row in h:
    try:
        row=str(row)
        row=row.encode('utf-8')
        payload = row
        #print row
        headers = {
            'content-type': "text/raw",
            'accept': "application/json",
            'x-ag-access-token': "YOUR KEY",
            'x-calais-language': "English",
            'outputformat': "application/json",
            'cache-control': "no-cache",
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        #print len(response.text)
        parsed_json = json.loads(response.text)
        docID=parsed_json['doc']['info']['docId']
        docID = str(docID)


        #cat1= parsed_json [docID+ "/cat/1"]["name"]
        #cat2= parsed_json [docID+ "/cat/2"]["name"]
        #cat3= parsed_json [docID+ "/cat/3"]["name"]
        tag1= parsed_json [docID+ "/SocialTag/1"]["name"]
        tag2= parsed_json [docID+ "/SocialTag/2"]["name"]
        tag3= parsed_json [docID + "/SocialTag/3"]["name"]
        tag4= parsed_json [docID + "/SocialTag/4"]["name"]
        #tag5= parsed_json [docID + "/SocialTag/5"]["name"]
        mydata=[[row,tag1,tag2,tag3,tag4]]
        #mydata=mydata.encode('utf-8')
        rr.writerows(mydata)
        print mydata

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
