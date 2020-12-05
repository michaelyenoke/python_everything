import requests
import pandas as pd

res = requests.get(url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-075?Authorization=CWB-7FA69130-059B-4028-8C38-51C1FCF9F72E&format=XML&startTime=')

box = []
box.append(res.text)

print(box)
