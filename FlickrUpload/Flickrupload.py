import os
import flickr_api
import json


flickr_api_key = '7472d48c4a6c47634077ce0146bf657a'
flickr_secret = 'a0fa65e064206044'

flickr_api.set_keys(api_key = flickr_api_key, api_secret = flickr_secret)
a = flickr_api.auth.AuthHandler()
perms = 'write'
url = a.get_authorization_url(perms)
print url
verification_code = raw_input("Enter verification code: ")
a.set_verifier(verification_code)
flickr_api.set_auth_handler(a)
a.save('auth_file')
print "Authenticated!"

with open("images.json", "r")  as read_file:
    data = json.load(read_file)
    i = 0
    while i < len(data):
        Title = data[i]['Title']
        filepath = data[i]['Filename']
        Common = data[i]['Common']
        Dept = data[i]['Dept']
        URL = data[i]['URL']
        Accession = data[i]['Accession']
        Title = Title + str(" ") + Common + str(" ") + Accession
        Tags = Dept + str(" ") + Accession + str(" ") +Common
        Description = Title + str(" from the ") + Dept + str(" department. For more details visit Collections Online - ") + URL

        flickr_api.upload(photo_file = filepath, title = Title, tags = Tags,description = Description, is_public="0")

        i = i + 1
