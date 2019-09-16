import colorgram
import csv
import urllib2
import webcolors
import cooperhewitt.roboteyes.colors.palette as palette
import cooperhewitt.swatchbook as sb
from roygbiv import * 
from PIL import Image

input_file =open('input.csv',"rb")
output_file =open('ouputcolorgram.csv',"ab")
writer = csv.writer(output_file)
   
for row in input_file:
    filename = urllib2.urlopen(row)
   
    def closest_colour(requested_colour):
        min_colours = {}
        for key, name in webcolors.css3_hex_to_names.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]
    
    def get_colour_name(requested_colour):
        try:
            closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
        except ValueError:
            closest_name = closest_colour(requested_colour)
            actual_name = None
        return actual_name, closest_name
    
    roy = Roygbiv(filename)
    ref = 'crayola'
    #print roy.get_palette_hex()
    rsp = palette.extract_roygbiv(filename, ref)
    print pprint.pformat(rsp)
    
    
   
   #extract 4 colours from the file
    colors = colorgram.extract(filename, 4)
    first_color = colors[0]
    second = colors[1]
    third = colors[2]
    forth = colors[3]
    print third
   
   #Convert each of the colours into RGB format
    rgb1 = first_color.rgb 
    rgb2 = second.rgb 
    rgb3 = third.rgb 
    rgb4 = forth.rgb
    
    #Convert RGB to HEX
    hex1 = '#%02x%02x%02x' % rgb1
    hex2 = '#%02x%02x%02x' % rgb2
    hex3 = '#%02x%02x%02x' % rgb3
    hex4 = '#%02x%02x%02x' % rgb4
    
   # get the % proportion 
    proportion1  = first_color.proportion 
    proportion2  = second.proportion 
    proportion3  = third.proportion 
    proportion4  = forth.proportion 
    
    #Get the closest named colour.
    actual_name1, closest_name1 = get_colour_name(rgb1)
    actual_name2, closest_name2 = get_colour_name(rgb2)
    actual_name3, closest_name3 = get_colour_name(rgb3)
    actual_name4, closest_name4 = get_colour_name(rgb4)
   
    #Combine
    colour1 = str(hex1) + str(", ") + str(hex2) + str(", ") + str(hex3) + str(", ") + str(hex4) + str("| ")
    colour2 = str(rgb1) + str(", ") + str(rgb2) + str(", ") + str(rgb3) + str(", ") + str(rgb4) + str("| ")
    colour3 = str(proportion1) + str(", ") + str(proportion2) + str(", ") + str(proportion3) + str(", ") + str(proportion4) + str("| ")
    colour4 = str(closest_name1) + str(", ") + str(closest_name2) + str(", ") + str(closest_name3) + str(", ") + str(closest_name4) + str("| ")
    colour5 = str(actual_name1) + str(", ") + str(actual_name2) + str(", ") + str(actual_name3) + str(", ") + str(actual_name4)
    final =  colour1 + colour2 + colour3 + colour4 + colour5
    
    #Write to CSV
    writer.writerow([row]+[final])
    #print final
