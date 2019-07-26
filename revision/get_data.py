"""
# import library python
import requests, json, csv, sys

# menghubungkan dengan URL
url = "https://api.exchangeratesapi.io/history?start_at=2019-06-03&end_at=2019-06-16&base=IDR"
response = requests.get(url)

# membaca hasilnya
data = response.text

# ubah string menjadi json
parsing_data = json.loads(data)

# print(json.dumps(parsed, indent=4))
if sys.argv[1] is not None and sys.argv[2] is not None:

    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]

    inputFile = open(fileInput)
    outputFile = open(fileOutput, 'w')
    data2 = json.load(inputFile)
    inputFile.close()

    output = csv.writer(outputFile)

    output.writerow(data[0].keys())

    for row in data2:
       output.writerow(row.values())"""

import json
from urllib.request import urlopen

with urlopen("https://api.exchangeratesapi.io/2019-01-01?symbols=USD,CNY&base=IDR") as url:
    source = url.read()

data = json.loads(source)

print(json.dumps(data, indent=2, sort_keys=True))
