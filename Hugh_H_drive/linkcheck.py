import csv
import requests
import pandas
import time
from collections import namedtuple
from tqdm import tqdm

infile  = "NS-check.csv"
outfile = "NS-check-resultsFeb12.csv"
headers = ["url"]

with open(infile, mode='r') as f:
    reader = csv.reader(f)
    
    all_records = namedtuple('rec', next(reader))
    records = [all_records._make(row) for row in reader]
    
    with open(outfile, mode='w+') as o:
        w = csv.writer(o)
        w.writerow(headers)
        
        num = len(records)
        print("Checking {} records...\n".format(num))
        
        with tqdm(total=num, bar_format="{percentage:3.0f}% {bar} [{n_fmt}/{total_fmt}]  ", ncols=64) as pbar:
            for r in records:
                pbar.update(1)
                # update the ".id" here according to the header of that column (or just rename the column to 'id')
                identifier = r.id
                # construct URL; update this according to the content type you're checking
                # url  = "https://api.aucklandmuseum.com/id/humanhistory/object/" + identifier
                url  = "https://api.aucklandmuseum.com/id/naturalsciences/object/" + identifier
                req  = requests.get(url, allow_redirects=False)
                code = req.status_code
                # only write 200s
                if code == 200:
                    w.writerow([url])
                    time.sleep(.25)
                else:
                    time.sleep(.25)

df = pandas.read_csv(outfile)
print("Found {} 200 OK statuses".format(len(df)))