#import simplejson

import json

with open('C:/Users/MichaelCHEN/Desktop/getweb.json','r') as f:
    json_data = json.load(f)
    
    
with open('/home/dktdatateamtaiwan/env/etl_jl_git/json_lines2.jl','w') as outfile:
  for entry in json_data:
    print(json_data)
    json.dump(entry, outfile)
    outfile.write('\n')
    #print(entry)
