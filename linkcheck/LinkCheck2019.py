import requests
import pandas
import time
from collections import namedtuple
from tqdm import tqdm
import csv
​
with open('in.csv', mode='r') as f:
    reader = csv.reader(f)
    
    all_records = namedtuple('rec', next(reader))
    records = [all_records._make(row) for row in reader]
    
    with open('out.csv', mode='w+') as o:
        w = csv.writer(o)
        w.writerow(["ContentItemId","code"])
        
        errors = 0
        ok = 0
        l = len(records)
        print("Checking {} records...\n".format(l))
        
        with tqdm(total=l, bar_format="{percentage:3.0f}% {bar} [{n_fmt}/{total_fmt}]  ", ncols=64) as pbar:
            for r in records:
                pbar.update(1)
                id   = r.ContentItemId
                url  = "https://api.aucklandmuseum.com/id/library/ephemera/" + id
                req  = requests.get(url, allow_redirects=False)
                code = req.status_code
                w.writerow([id, code])
                time.sleep(.25)
​
print ('\nSummary: ')
df = pandas.read_csv("out.csv")
print(df['code'].value_counts())
