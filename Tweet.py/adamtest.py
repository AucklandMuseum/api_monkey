import requests
import json, ast
import shutil
from datetime import datetime, timedelta
import time
import urllib
import tweepy
import settings
from PIL import Image
import urllib2
import os, re
import random,csv
# from pprint import pprint as pp
import csv
import pprint as pp

# input_file = open('twitterLog.csv',"rb")
# output_file = open('twitterLog.csv',"ab")
# writer = csv.writer(output_file)

def hashtags(dept):
    dept=dept.replace("'","")
    hashes=""
    hashdict={
        "Botany":['botany','nature','science','plants','image'],
        "Entomology":['entomology','nature','science','bugs','insects'],
        "photography":['photography','art','pics'],
        "Marine":['marine','nature','science','underwater'],
        "publication":['books','museum','library'],
        "Pacific/Ethnology":['pacific','heritage','museum'],
        "Applied Arts and Design":['AppliedArts','design','art','craft'],
        "History":['history','heritage','humanhistory','socialhistory','story'],
        "ephemera":['ephemera','heritage','archives','history'],
        "Archaeology":['archaeology','heritage','museum'],
        "birds/land vertebrates":['birds','nature','wildlife'],
        "Geology":['geology','science','enviroment'],
        "manuscripts and archives":['manuscripts','heritage','history','library'],
        "World/Ethnology":['world','heritage','museum'],
        "reptiles and amphibians/land vertebrates":['reptiles','nature'],
        "Maori/Ethnology":['maori','history','nz'],
        "painting and drawings":['paintings','heritage','art'],
        "land mammals/land vertebrates":['mammals','nature','animals'],
        "Ethnology":['ethnology','history','story'],
        "Pictorial":['Pictorial','heritage']
    }

    if hashdict.has_key(dept):
        l=hashdict[dept]
        for item in l:
            hashes=hashes+" #"+str(item)
        hashes=hashes+" "
    else:
        return "No Hashes"

    return hashes

def random_dept():
    depts = ['entomology', 'marine', 'publication', 'applied', 'history', 'ephemera', 'birds', 'geology', 'manuscripts', 'world', 'reptiles', 'painting', 'mammals']
    last_dept = None
    while 1:
        random.shuffle(depts)
        if depts[0] == last_dept:
            continue
        for item in depts:
            yield item
        last_dept = depts[-1]

Rando = iter(random_dept())
for _ in range(1):
    print(next(Rando))




def step1():

    depts = ['entomology', 'marine', 'publication', 'applied', 'history', 'ephemera', 'birds', 'geology', 'manuscripts', 'world', 'reptiles', 'painting', 'mammals']
    dept  = random.choice(depts)
    print "###############################START#################################################"
    print ("Department: " + dept)
    
    id = random.randrange(0, 1000, 2)
    print ("Random ID: ", id)
    # id = 4
    
    try:
        ###############################################################################
        url = "https://api.aucklandmuseum.com/search/collectionsonline/_search"
        
        querystring = {"size":"1000","pretty":"true"}
        
        #print (querystring)
        
        payload = "{\"sort\":[{\"lastModifiedOn\":{\"order\":\"desc\"}}],\"query\":{\"filtered\":{\"filter\":{\"bool\":{\"must\":[{\"term\":{\"department\":\""
        payload += dept
        payload += "\"}},{\"exists\":{\"field\":\"primaryRepresentation\"}}]}}}}}"
        
        #print (payload)
        
        headers = { 'Accept': "application/json",
                    'Content-Type': "application/json" }
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    
        #print ("Response: \n", response.text)
        #print ("hello")
        ###############################################################################
    
        parsed_json = json.loads(response.text)
        print parsed_json["hits"]["hits"][id]['_id']
        image_url = parsed_json["hits"]["hits"][id]['_source']['primaryRepresentation']
        image_url = ast.literal_eval(json.dumps(image_url))
        image_url = (str(image_url) + "?rendering=standard.jpg")
        image_url = (str(image_url).replace('[', '').replace(']',''))
        
        
        # Image checker begins:
        print ('Image URL: ' + image_url)
    
        # Get image metadata (at /media/v/[id]/metadata)
        img_querystring = {"rendering":"standard.jpg"}
        img_headers = {'Accept': "application/json"}
        image_response = requests.request("GET", image_url, headers=img_headers, params=img_querystring)
        image_json = json.loads(image_response.text)
        
        
        #Cultural Permissions
        try: 
            permissions = image_json['ecrm:P75_possesses'][0]['value'] 
            permissions_response = requests.request("GET", permissions, headers=img_headers, params=img_querystring)
            permissions_Json = json.loads(permissions_response.text)
            cultural_Permissons = permissions_Json['rdf:value'][0]['value']
            print cultural_Permissons

            if "CC BY" in cultural_Permissons or "No Known" in cultural_Permissons or " Out of" in cultural_Permissons:
                
                # Print it, just to check
                printable_img_json = ast.literal_eval(json.dumps(image_json))
                #print (printable_img_json)
                
                # Pull timestamp from image metadata as a string, turn it into a datetime object
                image_date = image_json['am:lastModifiedOn'][0]['value']
                image_date = ast.literal_eval(json.dumps(image_date))
                
                image_location = image_json['am:mediaLocation'][0]['value']
                image_location = ast.literal_eval(json.dumps(image_location))
                print (image_location)
                
                # Evaluate datetime object: was it a good year for AM collection images?
                date_format = "%Y-%m-%dT%H:%M:%S.%fZ" 
                dt_obj = datetime.strptime(image_date, date_format)
                print (dt_obj.year)

                if dt_obj.year == 2016 or 2017 or 2018 or 2019:
                    urllib.urlretrieve(image_url, "1.jpg")
                    img = Image.open("1.jpg")
                    dept = parsed_json["hits"]["hits"][id]['_source']['department']
                    dept = ast.literal_eval(json.dumps(dept))
                    print (dept)
                    print os.stat('1.jpg').st_size
                    if os.stat('1.jpg').st_size == 17015:
                        print ("Placeholder Image")
                    elif os.stat('1.jpg').st_size == 15411:
                        print ("Placeholder Image")
                    elif 'collection' or 'Entomology' in image_location or "Ephemera" in dept or "painting and drawings" in dept or "Pictorial" in dept:
                        print ("whoop")
                        url = parsed_json["hits"]["hits"][id]['_id']
                        title = parsed_json["hits"]["hits"][id]['_source']['appellation']['Primary Title']
                        title = ast.literal_eval(json.dumps(title))
                        dept = parsed_json["hits"]["hits"][id]['_source']['department']
                        dept = ast.literal_eval(json.dumps(dept))
                        rep = {
                            "http://api.aucklandmuseum.com/id/": "http://www.aucklandmuseum.com/collections-research/collections/record/",
                            "naturalsciences/object/": "am_naturalsciences-object-", "humanhistory/object/": "am_humanhistory-object-",
                            "library/ephemera/": "am_library-ephemera-", "library/photography/": "am_library-photography-",
                            "library/manuscriptsandarchives/": "am_library-manuscriptsandarchives-",
                            "library/paintinganddrawings/": "am_library-paintinganddrawings-",
                            "library/catalogq40/": "am_library-catalogq40-"}
                            
                        rep = dict((re.escape(k), v) for k, v in rep.iteritems())
                        pattern = re.compile("|".join(rep.keys()))
                        url = pattern.sub(lambda m: rep[re.escape(m.group(0))], url)
                        h=hashtags(str(dept).replace('[', '').replace(']',''))
                        
                        
                        tweet = str(title).replace('[', '').replace(']', '') + " from the " + str(dept).replace('[', '').replace(']','') + " department. " + str(h) + str(url)
                        
                        # Go Tweet!
                        auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
                        auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
                        api = tweepy.API(auth)
                        #api.update_with_media('1.jpg', str(tweet))
                        print (tweet)
            
                        #wait three hours
                        time.sleep(10800)
                    else:
                        print "location fail"
            else:
                print (":~{ not open image")
                
        except KeyError:
            print "No rights statment" 
            
    except ValueError:
            print "value Error"            

while True:
    step1()