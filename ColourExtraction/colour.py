import sys
import pprint
import cooperhewitt.roboteyes.colors.palette as palette
import cooperhewitt.swatchbook as sb
from roygbiv import * 
import csv
import urllib2
import urllib


input_file =open('input.csv',"rb")
output_file =open('LBOut.csv',"ab")
writer = csv.writer(output_file)
i = 0
for row in input_file:
    try:
        urllib.urlretrieve(row, "0.jpg")
        path = Image.open("0.jpg")
        roy = Roygbiv(path)
        
        
        crayola = 'crayola'
        Cray_rsp = palette.extract_roygbiv(path, crayola)
        Average_hex = Cray_rsp['average']['color']
        Crayola_Average = Cray_rsp['average']['closest']
        Crayola_Palette = Cray_rsp['palette']
       
        css3 = 'css3'
        Css3_rsp = palette.extract_roygbiv(path, css3)
        Css3_Average = Css3_rsp['average']['closest']
        Css3_Palette = Cray_rsp['palette']
        b = str("|")
        i = i + 1
        print i
    
        writer.writerow([row]+[Average_hex]+[Crayola_Average]+[Css3_Average]+[Crayola_Palette]+[b]+[Css3_Palette])
    
    except IOError:
        print "error"
