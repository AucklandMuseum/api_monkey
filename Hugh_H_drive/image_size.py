
# Auckland Museum Vernon AV file-size checker
# hlilly@aucklandmuseum.com
# February 2020

# Expects a list of Vernon AV IDs in a .csv. Checks image file sizes,
#   outputting a .csv that identifies images as either:
#     (a) a "not yet created" placeholder, or
#     (b) a "not available" placeholder, or
#     (c) a correctly processed image (with a note of its size)

import csv
import requests
import pandas
import time
from collections import namedtuple
from tqdm import tqdm

# Takes a single-column .csv file that is a list of
# Vernon AV IDs, with "id" as the column header.
infile  = "ImagesSinceNov_2nd-batch.csv"
outfile = "ImagesSinceNov_2nd-batch-results.csv"

# Open input file for reading
with open(infile, mode='r') as f:
    reader = csv.reader(f)
    
    # Create dictionary of contents
    all_records = namedtuple('rec', next(reader))
    records = [all_records._make(row) for row in reader]
    
    # Open output file for writing
    with open(outfile, mode='w+') as o:
        
        # Create writer object; write headers
        w = csv.writer(o)
        headers = ["id","type","size"]
        w.writerow(headers)
        
        # Print info to console
        num = len(records)
        print("Checking {} images...\n".format(num))
        
        # Create progress bar object, iterate over records in input file
        with tqdm(total=num, bar_format="{percentage:3.0f}% {bar} [{n_fmt}/{total_fmt}]  ", ncols=64) as pbar:
            for r in records:
                pbar.update(1)
                
                # Get AV ID from row in file; construct URL
                id = r.id
                url = "http://media.api.aucklandmuseum.com/id/media/v/" + str(id) + "?rendering=original.jpg"
                
                # Request headers; store file size as an integer
                req = requests.head(url, allow_redirects=False)
                size = int(req.headers['Content-Length'])

                # If "Not yet created" placeholder, write ID and "nyc", then sleep
                if size == 36121:
                    w.writerow([id, "nyc"])
                    time.sleep(.25)
                
                # Else, if "Not available", write such, then sleep
                elif size == 34681:
                    w.writerow([id, "na"])
                    time.sleep(.25)
                
                # Else, write id, blank column, and file size, then sleep
                else:
                    w.writerow([id,None,size])
                    time.sleep(.25)

# Construct pandas dataframe and print count of "nyc" column
df = pandas.read_csv(outfile)
count_nyc = df['type'].value_counts()['nyc']
print("Found {} NYC placeholders.".format(count_nyc))