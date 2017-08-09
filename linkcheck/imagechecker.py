import requests
import csv
import json

# list.csv should contain plain API image URLs, one per line
# e.g. http://api.aucklandmuseum.com/id/media/v/320810
#
# errors.csv will contain only those assets which return 404 statuses

total_errors = 0

with open('list.csv', "r+") as links:
    data = csv.reader(links)
    numrows = len(list(data))
    print "Opened a file with " + str(numrows) + " rows."
links.close()

with open('first20.csv', "r+") as links:

    # open file and list number of rows
    data = csv.reader(links)

    # for each row, check if 404
    for row in data:
        # render as string
        row = ''.join(row)
        # set headers, otherwise API sends image
        headers = {'accept': "application/json"}
        response = requests.get(row, headers=headers)
        # if 404, add URL to errors.csv; list total found so far.
        if response.status_code == 404:
            with open("errors.csv","ab") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([row])
            total_errors += 1
            print ("Error found at row " + str(data.line_num) + "." + " (" + str(total_errors) + (" error" if total_errors == 1 else " errors") + " so far.)")
        # if (numrows -1) == data.line_num:
        #     print "Reached the last line. Found " + str(total_errors) + " errors out of " + str(numrows) + " total rows."
links.close()
