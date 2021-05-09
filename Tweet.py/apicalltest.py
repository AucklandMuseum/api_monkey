import requests
import json
import random
import ast
import pprint as pp

depts = ['Entomology', 'photography', 'Marine', 'publication', 'Applied', 'History', 'ephemera', 'birds', 'Geology', 'manuscripts', 'World', 'reptiles', 'painting', 'mammals']
dept = random.choice(depts)
print "Random department is " + dept

# dept =  "ephemera"

###############################################################################
url = "https://api.aucklandmuseum.com/search/collectionsonline/_search"
querystring = {"default_operator": "AND", "q": "primaryRepresentation:http*+department%3A%22" + dept + "%22","size":"1"}
payload = "{\r\n\"sort\" : [\r\n{ \r\n\"lastModifiedOn\" : \r\n{\"order\" : \"desc\"} \r\n}\r\n]\r\n}\r\n"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "17fc23fc-aebf-2424-bca0-c3a850d08721"
}
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
###############################################################################

#print(response.text)
parsed_json = json.loads(response.text)
print parsed_json["hits"]["hits"][0]['_source']['department']
print parsed_json["hits"]["hits"][0]['_source']['primaryRepresentation']


# i = 0
# for i in parsed_json:
#     dept = parsed_json["hits"]["hits"][i]['_source']['department']
#     dept = ast.literal_eval(json.dumps(dept))
#     print dept
#     i =+ 1