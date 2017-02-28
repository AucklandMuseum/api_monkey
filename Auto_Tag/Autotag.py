from microsoftcognitive import MicrosoftVision
#import roygbiv
import csv
import json

f=open("a.csv","rb")
r=open("output.csv","ab")
rr=csv.writer(r)
h=csv.reader(f)
for row in h:
    print ''.join(row)

    mv = MicrosoftVision('[API KEY]',MicrosoftVision.VisualService.ANALYZE)
    mv.setFeatures({mv.VisualFeature.DESCRIPTION})
    result = mv.jsonRecognizeImageFromFile(row[0])
    print result
    data=json.loads(json.dumps(result,indent=4))
    print data
    #print data['description'].
    desc=data['description']['captions'][0]['text']
    tags=','.join(data['description']['tags'])
    #print desc,tags
    res=[''.join(row),desc,tags]
    rr.writerow(res)

f.close()
r.close()
