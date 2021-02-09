import simplejson

with open('/home/dktdatateamtaiwan/env/etl_jl_git/get.json','r') as f:
  json_data =simplejson.load(f)
  
with open('/home/dktdatateamtaiwan/env/etl_jl_git/json_lines2.jl','w') as outfile:
  for entry in json_data:
    simplejson.dump(entry, outfile)
    outfile.write('\n')
  
  
  
