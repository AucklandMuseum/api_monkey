import requests
import csv
import json

# list.csv should contain plain API image URLs, one per line
# e.g. http://api.aucklandmuseum.com/id/media/v/320810/metadata
#
# errors.csv will contain only those assets which return 404 statuses

total_errors = 0

# List total number of rows in file.
with open('list.csv', "r+") as links:
    data = csv.reader(links)
    numrows = len(list(data))
    print ("Your file contains " + str(numrows) + " rows." + '\n')
links.close()

# Open file, check for 404s
with open('list.csv', "r+") as links:

    data = csv.reader(links)

    # for each row, check if 404
    for row in data:
        
        # Convert to string
        row = ''.join(row)
        
        # Set headers, otherwise API sends images
        headers = {'accept': "application/json"}
        response = requests.get(row, headers=headers)
        
        # If 404, add URL to errors.csv and report tally.
        if response.status_code == 404:
            with open("first_20_errors.csv","ab") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([row])
            total_errors += 1
            print ("Error at row " + str(data.line_num) + "" + " (" + str(total_errors) + (" total error" if total_errors == 1 else " total errors") + " so far).")
        # Print report at end.
        if (numrows) == data.line_num:
            print ('\n' "Reached the end, having found " + str(total_errors) + " errors out of " + str(numrows) + " total rows.")
            
links.close()
