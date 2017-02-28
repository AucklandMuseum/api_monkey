__author__ = 'amoriarty'
import requests as re


class MicrosoftVision:

    __url = 'dfd'
    __header = {
        'Content-Type': '',
        'Ocp-Apim-Subscription-Key': '',
    }
    __parameters = {
        'visualFeatures': ''
    }

    def __init__(self,key,service='https://api.projectoxford.ai/vision/v1.0/analyze?'):
        self.__header['Ocp-Apim-Subscription-Key'] = key
        self.__url = service


# Image features extraction Constants
    class VisualFeature:
        CATEGORIES = 'Categories'
        COLOR = 'Color'
        TAGS = 'Tags'
        DESCRIPTION = 'Description'
        FACES = 'Faces'
        IMAGETYPE = 'ImageType'
        ADULT = 'Adult'

# Different Microsoft Vision Services
    class VisualService:
        ANALYZE = 'https://api.projectoxford.ai/vision/v1.0/analyze?'
        DESCRIBE = 'https://api.projectoxford.ai/vision/v1.0/describe?'

# Additional Details to extract from Image
    class VisualDetails:
        CELEBRITIES = 'Celebrities'

    def jsonRecognizeImageFromURL(self,url):
        self.__header['Content-Type'] = 'application/json'
        json = {'url':url}
        data = None
        result = self.__postProcessRequest(json,data,self.__header,self.__parameters)
        return result

    def jsonRecognizeImageFromFile(self,file):
        with open(file,'rb') as f:
            data = f.read()
        self.__header['Content-Type'] = 'application/octet-stream'
        json = None
        result = self.__postProcessRequest(json,data,self.__header,self.__parameters)
        return result


    def setFeatures(self,paramaterlist):
        __parameterlist =  ','.join(paramaterlist)
        self.__parameters = { 'visualFeatures':__parameterlist}


    def getFeatures(self):
        return self.__parameters


    def __processRequest(self,json,data,headers,params):
       return re.request('post', self.__url, json=json, data=data, headers=headers, params=params)


    def __postProcessRequest(self,json, data, headers, params):
        __result = self.__processRequest(json,data,headers,params)
        if (__result.status_code == 400):
            jsn = __result.json()
            print 'Error: 404', '\n', 'Code:', jsn['code'], '\n', 'Message:', jsn['message']

        elif (__result.status_code == 415):
            print 'Error: 415', '\n', 'The image provided is not in a valid format'

        elif (__result.status_code == 200):
            result = __result.json()

        return result

    def getImageName(self,json):
        __json = json
