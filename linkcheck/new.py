__author__ = 'adam'
import urllib2
import csv

total_errors = 0

# List total number of rows in file.
with open('list.csv', "r+") as links:
    data = csv.reader(links)
    numrows = len(list(data))
    print ("Your file contains " + str(numrows) + " rows." + '\n')
links.close()

with open('list.csv', "r+") as links:

    data = csv.reader(links)

    # for each row, check if 404
    for row in data:

        # Convert to string
        row = ''.join(row)

        f = urllib2.urlopen(row)
        size= f.headers["Content-Length"]
        #print size
        if size == "36121":
            with open("first_20_errors.csv","ab") as outfile:
                writer = csv.writer(outfile)
                writer.writerow([row])
            total_errors += 1
            print ("Error at row " + str(data.line_num) + "" + " (" + str(total_errors) + (" total error" if total_errors == 1 else " total errors") + " so far).")
        # Print report at end.
        if (numrows) == data.line_num:
            print ('\n' "Reached the end, having found " + str(total_errors) + " errors out of " + str(numrows) + " total rows.")

links.close()
