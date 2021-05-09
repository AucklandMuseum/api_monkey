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

#http://media.api.aucklandmuseum.com/id/media/v/1476?rendering=original.jpg
#https://api.aucklandmuseum.com/id/media/p/17e89ff5c7cd456262744aa75ec9f24add55a597?rendering=original.jpg


image_url = "https://media.api.aucklandmuseum.com/id/media/v/553905?rendering=original.jpg"
urllib.urlretrieve(image_url, "1.jpg")

size = os.stat('1.jpg').st_size
print size

image_file = '1.jpg'
img_org = Image.open(image_file)
width_org, height_org = img_org.size
factor = 0.75
width = int(width_org * factor)
height = int(height_org * factor)
img5 = img_org.resize((width, height), Image.ANTIALIAS)
ext = ".jpg"
img5.save("ANTIALIAS" + ext)
new_size = os.stat('ANTIALIAS.jpg').st_size
print new_size

3000000
1412330