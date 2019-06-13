import json
from clarifai.rest import ClarifaiApp
from clarifai.rest import Workflow
from clarifai.rest import Image as ClImage
import csv 

# The CSV file should be URL links
f=open("input.csv","rb")
r=open("output.csv","ab")
rr=csv.writer(r)
h=csv.reader(f)



for row in h:
    #print ''.join(row)
    app = ClarifaiApp(api_key='KEY')
    workflow = Workflow(app.api, workflow_id="WORKFLOW")
    image = ClImage(url=(row[0]))
    response = workflow.predict([image])
    print json.dumps(response)
    concepts = response['results'][0]['outputs'][1]['data']['concepts']
    colours = response['results'][0]['outputs'][0]['data']['colors']
    l = len(colours)

    
    t0 = (concepts[0]['name'], concepts[0]['value'])
    t1 = (concepts[1]['name'], concepts[1]['value'])
    t2 = (concepts[2]['name'], concepts[2]['value'])
    t3 = (concepts[3]['name'], concepts[3]['value'])
    t4 = (concepts[4]['name'], concepts[4]['value'])
    t5 = (concepts[5]['name'], concepts[5]['value'])
    t6 = (concepts[6]['name'], concepts[6]['value'])
    t7 = (concepts[7]['name'], concepts[7]['value'])
    t8 = (concepts[8]['name'], concepts[8]['value'])
    t9 = (concepts[9]['name'], concepts[9]['value'])
    t10 = (concepts[10]['name'], concepts[10]['value'])
    Tags = str(t1)+ str(t2) + str(t3) + str(t4) + str(t5) + str(t6) + str(t7) + str(t8) + str(t9) + str(t10)
   

    
    
    if l == 1 :
        c1 =(colours[0]['w3c']['hex'],colours[0]['w3c']['name'] )
        Final = str(Tags) + str(c1) 
        res = str(row) + str(Final)
        print res
        rr.writerow([res])
    else:
        if l == 2:
            c1 =(colours[0]['w3c']['hex'],colours[0]['w3c']['name'] )
            c2 =(colours[1]['w3c']['hex'],colours[1]['w3c']['name'] )
            Final = str(Tags) + str(c1) + str(c2) 
            res = str(row) + str(Final) + str(Tags)
            print res
            rr.writerow([res])
        else:
            if l == 3 :
                c1 =(colours[0]['w3c']['hex'],colours[0]['w3c']['name'] )
                c2 =(colours[1]['w3c']['hex'],colours[1]['w3c']['name'] )
                c3 =(colours[2]['w3c']['hex'],colours[2]['w3c']['name'] )
                Final = str(Tags) + str(c1) + str(c2) + str(c3)
                res = str(row) + str(Final) + str(Tags)
                print res
                rr.writerow([res])
            else:
                if l >= 4:
                    c1 =(colours[0]['w3c']['hex'],colours[0]['w3c']['name'] )
                    c2 =(colours[1]['w3c']['hex'],colours[1]['w3c']['name'] )
                    c3 =(colours[2]['w3c']['hex'],colours[2]['w3c']['name'] )  
                    c4 =(colours[3]['w3c']['hex'],colours[3]['w3c']['name'] )
                    Final = str(Tags) + str(c1) + str(c2) + str(c3) + str(c4)
                    res = str(row) + str(Final) + str(Tags)
                    print res
                    rr.writerow([res])

f.close()
r.close()
