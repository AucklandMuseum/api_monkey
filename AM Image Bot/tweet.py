import requests
import json, ast
import shutil 
import time
import urllib
import tweepy
import settings
import Image
import urllib2
import os, re
import random

def step1():
  id= random.randrange(0, 101, 2)
  ###############################################################################
  url = "http://api.aucklandmuseum.com/search/collectionsonline/_search"
  querystring = {"q":"primaryRepresentation:http*&size=100&department:publication"}
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
  image0= parsed_json ["hits"]["hits"][id]['_source']['primaryRepresentation']
  image0 = ast.literal_eval(json.dumps(image0))
  image0 = image0 + "?rendering=standard.jpg"
  print image0
  urllib.urlretrieve(image0, "0.jpg")
  img = Image.open("0.jpg")

  if os.stat('0.jpg').st_size ==17015:
      print "Restart"
  elif os.stat('0.jpg').st_size ==15411:
      print "Restart again"
  else: 
      print "whoop"
      url = parsed_json ["hits"]["hits"][id]['_id']
      dept = parsed_json ["hits"]["hits"][id]['_source']['department']
      title = parsed_json ["hits"]["hits"][id]['_source']['appellation']['Primary Title']
      title =ast.literal_eval(json.dumps(title))
      rep ={"http://api.aucklandmuseum.com/id/":"http://www.aucklandmuseum.com/collections-research/collections/record/","naturalsciences/object/":"am_naturalsciences-object-","humanhistory/object/":"am_humanhistory-object-","library/ephemera/" :"am_library-ephemera-","library/photography/":"am_library-photography-","library/manuscriptsandarchives/":"am_library-manuscriptsandarchives-","library/paintinganddrawings/":"am_library-paintinganddrawings-","library/catalogq40/":"am_library-catalogq40-"}
      rep = dict((re.escape(k), v) for k, v in rep.iteritems())
      pattern = re.compile("|".join(rep.keys()))
      url = pattern.sub(lambda m: rep[re.escape(m.group(0))], url)
      tweet = str(title).replace('[', '').replace(']', '') + str(url)
      auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
      auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
      api = tweepy.API(auth)
      api.update_with_media('0.jpg',str (tweet))
      print tweet
      time.sleep(600)

while True:
    step1()
