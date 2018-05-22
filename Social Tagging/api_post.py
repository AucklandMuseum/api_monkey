__author__ = 'AMoriarty'
import requests
import csv
csvfile = open('file.csv', 'r')
url = "https://api.aucklandmuseum.com/tag"
fieldnames = ("subject","api")
reader = csv.DictReader( csvfile, fieldnames)

for row in reader:
    subject= (row['subject'])
    tag=(row['api'])
    payload = "{\n \"subject\": \"" +subject + "\",\n  \"tag\": \""+tag+"\"\n}"
    print payload
    headers = {
        'content-type': "application/json",
        'x-api-key': "YOUR KEY",
        'cache-control': "no-cache",
        'postman-token': "5434909a-79da-278d-6295-7495efea94dd"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
