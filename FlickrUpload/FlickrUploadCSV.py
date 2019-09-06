import os
import flickr_api
import json
import yaml
from urllib import urlopen
# from pprint import pprint as pp

config_file = 'auth.yaml'
with open(config_file, 'r') as config_file:
    config = yaml.load(config_file)
    flickr_api_key = config['flickr']['consumer_key']
    flickr_secret = config['flickr']['consumer_secret']

flickr = flickr_api.set_keys(api_key = flickr_api_key, api_secret = flickr_secret)
flickr_api.set_auth_handler('auth_file')
user = flickr_api.test.login()
print "Logged in as " + (user.username) + " (" + (user.id) + ")."

def get_data(data,i):
            try:
                print data['results']['bindings'][i]['medium']['value']
                medium = (data['results']['bindings'][i]['medium']['value'])
                medium = medium.replace(' ','-')
                print data['results']['bindings'][i]['format']['value']
                format = (data['results']['bindings'][i]['format']['value'])
                format = format.replace(' ','-')
                return medium,format
            except KeyError:
                pass

with open("data_single.json", "r", ) as read_file:
    data = json.load(read_file)
    i = 0
    try:
        while i < len(data):
            flickr_title = (data['results']['bindings'][i]['title']['value']).capitalize()
            print "Title: " + (flickr_title)

            filepath = (data['results']['bindings'][i]['image']['value'])
            filehandler = urlopen(filepath)
            print "Image URL: " + (filepath)

            medium,format = get_data(data,i)
            tags_to_upload = "painting no-known-copyright" + medium + " " + format
            print "Tags: " + (tags_to_upload)

            desc = (data['results']['bindings'][i]['desc']['value']).capitalize() + (data['results']['bindings'][i]['notes']['value']).capitalize()
            print (desc)

            photo_file = filepath
            # flickr_api.upload(photo_file = "test1308.jpg", photo_file_data = filehandler, title = flickr_title, tags = tags_to_upload, description = desc, is_public = "0")
            i = i + 1
    except flickr_api.FlickrError as ex:
        print("Error code:")
    i = i + 1
