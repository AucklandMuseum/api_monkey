import os
import requests
import json as simplejson
import settings

keyword='teaspoon'

AMrecord = requests.get('http://api.aucklandmuseum.com/v1/search/collectionsonline/_search?api_key='+settings.AM_API_KEY+'&q=%22'+keyword+'%22+primaryRepresentation:http*&size=1')

data = simplejson.loads(AMrecord.text)

print(data)