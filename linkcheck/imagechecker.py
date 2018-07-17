__author__ = 'adam'
import urllib2
import csv

################################################################################################
#This designed to check the full sized images. You should be using media.api.aucklandmuseum.com#
################################################################################################

input_file ='input.csv' # List should be a csv, using the format  - http://media.api.aucklandmuseum.com/id/media/v/Image_ID?rendering=original.jpg
output_file ='outputcsv' # this file will contain a list of broken images.
http://media.api.aucklandmuseum.com/id/media/v/531216?rendering=original.jpg
################################################################################################
#                            DO NOT EDIT BELOW                                                 #
################################################################################################

total_errors = 0

# List total number of rows in file.
with open(input_file, "r+") as links:
    data = csv.reader(links)
    numrows = len(list(data))
    print ("Your file contains " + str(numrows) + " rows." + '\n')
links.close()

with open(input_file, "r+") as links:

    data = csv.reader(links)

    # for each row, check if 404
    for row in data:

        # Convert to string
        row = ''.join(row)

        f = urllib2.urlopen(row)
        size= f.headers["Content-Length"]
        #print size
        if size == "36121":
            with open(input_file,"ab") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([row])
            total_errors += 1
            print ("Error at row " + str(data.line_num) + "" + " (" + str(total_errors) + (" total error" if total_errors == 1 else " total errors") + " so far).")
        if size == "34681":
            with open(output_file,"ab") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([row])
            total_errors += 1
            print ("Restricted at row " + str(data.line_num) + "" + " (" + str(total_errors) + (" total error" if total_errors == 1 else " total errors") + " so far).")
        # Print report at end.
        if (numrows) == data.line_num:
            print ('\n' "Reached the end, having found " + str(total_errors) + " errors out of " + str(numrows) + " total rows.")

links.close()
