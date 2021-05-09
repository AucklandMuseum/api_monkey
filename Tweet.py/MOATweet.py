import json
import urllib
import tweepy
import moasettings 
from PIL import Image
import urllib2
import os, re
import time

CONSUMER_KEY = '5SwHoavMbVvKZCYBl02Nlc3z4'
CONSUMER_SECRET = '2f1vok0DHXhzBlbDKEbzlVbhTnK6ycJ29UC9F3Vr0pLAa7w8Dw'
ACCESS_KEY = '1240409376612970497-t164xK4KTUeUH8IyjSU3bWKoH6Hyfn'
ACCESS_SECRET ='CJPxEabmhFTjXNqtQz4BdkcCNm2G0Z1pFJZnA6YiHRN7e'





with open('moaupload.json') as f:
  data = json.load(f)
  i = 0
  for p in data:
        try:
                title = data[i]['title']
                image_url = data[i]['image']
                org = data[i]['org']
                link = data[i]['link']
                i = i + 1
                tweet1 = str("Title: ") + title + str(". From the ") + org + str(" Collection. For more information visit - ") + link + str(".     #cat #catsOfAuckland")
                tweet = str(tweet1)
                print (tweet)
                urllib.urlretrieve(image_url, "cat.jpg")
                img = Image.open("cat.jpg")
                if os.stat('cat.jpg').st_size == 34681: #for standard.jpg use 17015
                        print ("Placeholder Image")
                elif os.stat('cat.jpg').st_size == 36121: #for standard.jpg use 15411 
                        print ("Placeholder Image")
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                api = tweepy.API(auth)          
                try:
                        if os.stat('cat.jpg').st_size > 3000000:
                                #print 'resize image'
                                image_file = 'cat.jpg'
                                img_org = Image.open(image_file)
                                width_org, height_org = img_org.size
                                factor = 0.75
                                width = int(width_org * factor)
                                height = int(height_org * factor)
                                img5 = img_org.resize((width, height), Image.ANTIALIAS)
                                ext = ".jpg"
                                img5.save("resizedcat" + ext)
                                api.update_with_media('resizedcat.jpg', str(tweet))
                                print (tweet)
                                #wait three hours
                                time.sleep(10800)
                        else:
                                api.update_with_media('cat.jpg', str(tweet))
                                print (tweet)
                                time.sleep(10800)
                except Error:
                        print "tweet error"
                except IOError:
                        print "tweet error"
        except UnicodeEncodeError:
                print "unicode error"
        except IOError:
                print "tweet error"