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
from pprint import pprint as pp

def hashtags(dept):
    dept=dept.replace("'","")
    #print dept
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

def step1():
    id = random.randrange(0, 1000, 2)
    ###############################################################################
    url = "https://api.aucklandmuseum.com/search/collectionsonline/_search"
    querystring = {"q": "primaryRepresentation:http*+-department:%22Botany%22&size=1000"}
    payload = "{\r\n\"sort\" : [\r\n{ \r\n\"lastModifiedOn\" : \r\n{\"order\" : \"desc\"} \r\n}\r\n]\r\n}\r\n"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "17fc23fc-aebf-2424-bca0-c3a850d08721"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    ###############################################################################

    # print(response.text)
    parsed_json = json.loads(response.text)
    image_url = parsed_json["hits"]["hits"][id]['_source']['primaryRepresentation']
    image_url = ast.literal_eval(json.dumps(image_url))
    image_url = image_url + "?rendering=standard.jpg"
    # Image checker begins:
    print 'Image URL: ' + image_url
    
    # Get image metadata
    # NB: Metadata actually resides at /media/v/[id]/metadata
    img_querystring = {"rendering":"standard.jpg"}
    img_headers = {'Accept': "application/json"}
    image_response = requests.request("GET", image_url, headers=img_headers, params=img_querystring)
    image_json = json.loads(image_response.text)
    
    # Print it, just to check
    printable_img_json = ast.literal_eval(json.dumps(image_json))
    #pp (printable_img_json)
    
    # Pull timestamp from image metadata as a string, turn it into a datetime object
    image_date = image_json['am:lastModifiedOn'][0]['value']
    image_date = ast.literal_eval(json.dumps(image_date))
    
    image_location = image_json['am:mediaLocation'][0]['value']
    image_location = ast.literal_eval(json.dumps(image_location))
    print image_location
    
    # Evaluate datetime object: was it a good year for AM collection images?
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ" 
    dt_obj = datetime.strptime(image_date, date_format)
    print dt_obj.year
    if dt_obj.year == 2016 or 2017 or 2018 or 2019:
        #print image0
        urllib.urlretrieve(image_url, "1.jpg")
        img = Image.open("1.jpg")
        dept = parsed_json["hits"]["hits"][id]['_source']['department']
        dept = ast.literal_eval(json.dumps(dept))
    
        if os.stat('1.jpg').st_size == 17015:
            print ("Restart")
        elif os.stat('1.jpg').st_size == 15411:
            print ("Restart again")
        elif 'Botany' in dept:
            print ("Sorry Botany...try again")
        elif 'Archaeology' in dept:
            print ("sorry Archaeology")
        elif 'Collection Imaging' in image_location or "Ephemera" in dept or "painting and drawings" in dept or "Pictorial" in dept:
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
            
            #send off to twitter
            auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
            auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_with_media('1.jpg', str(tweet))
            print (tweet)
            
            #wait three hours
            time.sleep(10800)

        else:
            print "bugger"

while True:
    step1()
