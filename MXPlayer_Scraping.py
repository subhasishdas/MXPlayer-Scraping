import requests
import csv
import json

params = {
  "api_key": "tP9GZdGfjakQ",
  "format": "json"
}
r = requests.get('https://www.parsehub.com/api/v2/runs/t5D2FDtC-gUn/data', params=params)
#print(r.text)
data = json.loads(r.text)

with open('dataset_2.csv', 'a', newline='') as csvFile:
    writer = csv.writer(csvFile)
    for p1 in data['selection1']:
        print('Website: ' + p1['name'])
        if p1['name']=="Live Channels":
            continue
        coll=p1['selection2']
        for p in coll:
            row1=[]
            row1.append(p1['name'])
            print('Show Name '+ p['name'])
            row1.append(p['name'])
            print('url '+ p['url'])
            row1.append(p['url'])
            print('url '+ p['selection3'])
            row1.append(p['selection3'])
            print('url '+ p['selection3_url'])
            row1.append(p['selection3_url'])
            writer.writerow(row1)
csvFile.close() 
