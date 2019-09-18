#!/usr/bin/env python
# -*- # coding: latin-1 -*-
import os
import flickr_api
import json
import urllib
import time

flickr_api_key = ''
flickr_secret = ''

flickr_api.set_keys(api_key=flickr_api_key, api_secret=flickr_secret)
#a = flickr_api.auth.AuthHandler()
#perms = 'write'
#url = a.get_authorization_url(perms)
#print url
#verification_code = raw_input("Enter verification code: ")
#a.set_verifier(verification_code)
#flickr_api.set_auth_handler(a)
#a.save('auth_file')
#print "Authenticated!"
flickr_api.set_auth_handler("auth_file")

with open("DH.json", "r") as read_file:

    data = json.load(read_file)
    i = 0
    try:
        while i < len(data):
            Title = data[i]['title']
            filepath = data[i]['filepath']
            #file = filepath.replace('S:\Collection Imaging\Hub photos clearance needed by Zoe\Human History', '')
            Titletag =Title.replace(' ','-')
            Titletag =Titletag.replace(',','')
            print Titletag
            print file
            Tags = data[i]['tags']
            #Tags = str("Natural-Science") +str(" ") + str("CC-BY") +str(" ") + Titletag
            Description = data[i]['Description']

            #use for API
            filehandler = urllib.urlopen(filepath)
            flickr_api.upload(photo_file = filepath, photo_file_data=filehandler, title = Title, tags = Tags, description = Description, is_public="0")

            #use for local filepaths
            # flickr_api.upload(photo_file = filepath, title = Title, tags = Tags, description = Description, is_public="0")
            i = i + 1
            time.sleep(30)
    except flickr_api.FlickrError as ex:
        print("Error code:")
        print filepath
        print ex
        i = i + 1

