import requests
import json
import flickr_api
from functions import *
import time


def parsePersistentURL(idNum):
  '''
  returns persistent url from metadata in flickr
  '''
  prefix = 'https://www.loc.gov/resource/'
  info = (flickr_api.Photo(id=idNum)).getInfo()['description']
  if info.find('item', info.find('Higher resolution'), info.find('</a>', info.find('Higher resolution'))) != -1:
    print(type(info.find('"', info.find('http:', info.find('Higher resolution')))))
    print(type(info.find('http:', info.find('Higher resolution')) + 7))
    return info[info.find('http:', info.find('Higher resolution')):info.find('"', info.find('http:', info.find('Higher resolution'))) - 1]
  else:
    endOfURL = info.find('</a>', info.find('Persistent URL'))
    indexOfURL = info.rfind('pnp/', 0, endOfURL) + 4
    if indexOfURL == -1:
      return None
    return prefix + info[indexOfURL:endOfURL]


existingJson = []
with open('local.json') as json_data:
  existingJson = json.load(json_data)
print(len(existingJson))
KEY = 'b13230b76c2db5780a32226fe3ee10d7'
SECRET = '0536c803405436d4'
# get keys here https://www.flickr.com/services/api/misc.api_keys.html
flickr_api.set_keys(api_key=KEY, api_secret=SECRET)

user = flickr_api.Person.findByUserName('aucklandmuseum_collections')
pages = user.getPublicPhotos().info.pages

firstPage = int(input('Enter first page number to search: '))
lastPage = int(input('Enter last page number to search: '))
if firstPage <= lastPage and firstPage >= 1 and lastPage <= pages:
  apiHits = 0  # prevents program from overloading flickr
  for i in range(firstPage, lastPage + 1):  # pages searched
    apiHits += 100  # every page contains 100 items
    photos = user.getPublicPhotos(page=i)
    if apiHits == 3600:  # the maximum number of api calls per hour is 3600
      time.sleep(3600)
      apiHits = 0
    urls = []
    for photo in photos:
      urls.append(parsePersistentURL(photo['id']))
    for url in urls:
      appendToList(url, existingJson)

  with open('local.json', 'w') as writefile:
    json.dump(existingJson, writefile)

  print('finished')
else:
  print('Invalid input')
