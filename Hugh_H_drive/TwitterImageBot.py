#TODO: Log things like response.status_code, tweet text etc. -- with timestamps

import urllib, urllib2, requests, json, ast, shutil, time, tweepy
import os, json, re, random, csv, pprint, settings
from datetime import datetime, timedelta
from PIL import Image

def get1000():
    global response
    url = 'https://api.aucklandmuseum.com/search/collectionsonline/_search'
    querystring = {"q": "primaryRepresentation:http*&size=1000"}
    payload = "{\r\n\"sort\" : [\r\n{ \r\n\"lastModifiedOn\" : \r\n{\"order\" : \"desc\"} \r\n}\r\n]\r\n}\r\n"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "17fc23fc-aebf-2424-bca0-c3a850d08721"}
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print 'Got the 1,000 most recently updated records.'
    return response

def getRandomID():
    global rand_id
    rand_id = random.randrange(0, 1000, 2)
    return rand_id

def getImageURL(jsontext, rand_id):
    global image_url
    print 'Getting random image...'
    # Parse JSON output and get image URL
    image_url = jsontext["hits"]["hits"][rand_id]['_source']['primaryRepresentation']
    ##### Would this work with +=? instead, or ''.join ?
    image_url = image_url + "?rendering=standard.jpg"
    return image_url

def getDept(jsontext, rand_id):
    global dept
    # Get department, store as a variable
    dept = jsontext["hits"]["hits"][rand_id]['_source']['department']
    dept = str(dept).replace('[u\'', '').replace('\']','')
    return dept
    
def getTitle(jsontext, rand_id):
    global title
    # Get title, store as a variable
    title = jsontext["hits"]["hits"][rand_id]['_source']['appellation']['Primary Title']
    title = str(title).replace('[u\'', '').replace('\']', '')
    return title

def getImageMetadata():
    global image_json
    ## Image checker begins ##
    try:
        #Set query string, headers
        img_querystring = {"rendering":"standard.jpg"}
        img_headers = {'Accept': "application/json"}
        # Send request, check for erorrs
        image_response = requests.request("GET", image_url, headers=img_headers, params=img_querystring, timeout=3)
        image_response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
            print ("Error while retrieving:", err)
    # Print HTTP response code (should be "200 OK")
    print '\nGetting image metadata...'
    print 'Image metadata response code:', image_response.status_code
    
    image_json = json.loads(image_response.text)
    return image_json

def getRightsStatement():
    # Get URL where rights statement resides
    global rights_statement
    try:
        rights_URL = image_json["ecrm:P75_possesses"][0]['value']
        print '\nGetting', rights_URL, '...'
        
        # Set query string, headers
        img_headers = {'Accept': "application/json"}
        
        # Send request, check for erorrs
        rights_metadata = requests.request("GET", rights_URL, headers=img_headers, timeout=3)    
        rights_metadata_json = json.loads(rights_metadata.text)
        
        # Assign rights statement to variable
        rights_statement = rights_metadata_json["rdf:value"][0]['value']
        print 'ecrm:P75_possesses value:', rights_statement
        return rights_statement
    except KeyError as errk:
        print 'Key error:', errk
        print "Record likely has no 'ecrm:P75_posseses' value.\n"
        rights_statement = 'No data'
        return rights_statement
    except ValueError as errv:
        print 'Value error:', errv
        print "Record likely has no 'ecrm:P75_posseses' value.\n"
        rights_statement = 'No data'
        return rights_statement

def isCulturalPermissions():
    global cultural_permissions
    if 'Cultural' in rights_statement:
        cultural_permissions = True
        print 'Cultural permissions?', cultural_permissions
        print 'Starting over...\n'
        return cultural_permissions
    else:
        cultural_permissions = False
        print 'Cultural permissions?', cultural_permissions
        return cultural_permissions

def getImageYear():
    global imageYear
    # Pull timestamp from image metadata as a string
    image_date = image_json['am:lastModifiedOn'][0]['value']
    image_date = ast.literal_eval(json.dumps(image_date))
    
    # Turn it into a datetime object
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ" 
    dt_obj = datetime.strptime(image_date, date_format)
    print '\nImage was last modified in ' + str(dt_obj.year) + "."
    # Assign it and return it
    imageYear = dt_obj.year
    return imageYear

def checkFilesize():
    global fileOK
    # Download image, check its size:
    urllib.urlretrieve(image_url, "0.jpg")
    if os.stat('0.jpg').st_size == 17015:
        print 'Image is only a placeholder (17015); trying again.\n'
        fileOK = False
    elif os.stat('0.jpg').st_size == 15411:
        print 'Image is only a placeholder (15411); trying again.\n'
        fileOK = False
    else:
        fileOK = True
        print 'File size OK.'
        return fileOK

def makeHashtagList(dept):
    dept = dept.replace("'","")
    hashes = ''
    hashdict={
        "botany":['botany','nature','science','plants','image'],
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
        l = hashdict[dept]
        for item in l:
            hashes = hashes + ' #' + str(item)
        hashes = hashes + ' '
    else:
        return 'No hashes'

    return hashes

def compileRecordURL(jsontext, rand_id):
    global record_url
    url = jsontext["hits"]["hits"][rand_id]['_id']
    rep = {
    "http://api.aucklandmuseum.com/id/": "http://www.aucklandmuseum.com/collections-research/collections/record/",
    "naturalsciences/object/": "am_naturalsciences-object-", "humanhistory/object/": "am_humanhistory-object-",
    "library/ephemera/": "am_library-ephemera-", "library/photography/": "am_library-photography-",
    "library/manuscriptsandarchives/": "am_library-manuscriptsandarchives-",
    "library/paintinganddrawings/": "am_library-paintinganddrawings-",
    "library/catalogq40/": "am_library-catalogq40-"}
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    record_url = pattern.sub(lambda m: rep[re.escape(m.group(0))], url)
    return record_url

def compileTweet():
    global tweet
    print '\nCompiling tweet...'
    # Use function to make list of hashtags
    hashtags = makeHashtagList(str(dept).replace('[', '').replace(']',''))
    
    # Compile text of tweet into a single variable, which we then return
    tweet = '\"' + title + "\" from the " + dept + " department." + str(hashtags) + str(record_url)
    return tweet

def doTweet(tweet):
    # Authorise
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    api = tweepy.API(auth)
    
    # Tweet
    api.update_with_media('0.jpg', str(tweet))
    print 'Tweet text: '
    print (tweet)

    # Update console and sleep
    print '\n******************  AMI bot is sleeping for  ******************'
    print '******************   the next three hours    ******************'
    time.sleep(10800)
    return

# This function for testing purposes only -- will not send tweet
def onlyPrintTweet(tweet):
    print 'Tweet text would be:'
    print (tweet)
    print '\nSuccess! Performing another test in 15 seconds...\n'
    time.sleep(15)
    return

def startBot():
    print '****************** Auckland Museum Image Bot ******************'
    
    # Get 1,000 most recently updated records
    get1000()
    
    # Make that data parseable
    jsontext = json.loads(response.text)
    
    # Generate a random number in order to randomly select a record
    getRandomID()
    print 'Record selected. Random number is', rand_id

    getTitle(jsontext, int(rand_id))
    print '\nRecord title: ', title
    
    getDept(jsontext, rand_id)
    # Stop botany posts
    if 'botany' in dept:
        print 'Got a botany record; trying again...'
    else:
        compileRecordURL(jsontext, int(rand_id))
        print 'Record URL:', record_url
        print 'Department: ', dept
        
        # Get image URL using from that random position in the results
        print '\nParsing JSON to get image URL...'
        getImageURL(jsontext, int(rand_id))
        
        # Get image metadata JSON (stored separately from main data)
        getImageMetadata()
        print 'Image URL: '+ image_url
        
        # Get rights statement (which is again stored separately)
        getRightsStatement()
        
        print 'Checking rights statement...'
        if isCulturalPermissions() == False:
            getImageYear()
            if imageYear == 2016 or 2017 or 2018:
                if checkFilesize() == True:
                    # All tests passed; ready to compile tweet
                    compileTweet()

                    # Comment-out one or the other of these lines
                    onlyPrintTweet(tweet)
                    # doTweet(tweet)
            else:
                print 'Photo not new enough; starting again.'

while True:
    startBot()
