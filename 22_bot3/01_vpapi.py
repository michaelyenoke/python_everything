import json
import requests
import pandas as pd
import datetime
import boto3
from io import StringIO # python3; python2: BytesIO 

def readapi(ticket,url):
    box = []
    ticket_input = ['ticketNO.','ticketNO.', 'ticketNO.', 'ticketNO.', 'ticketNO.', 'ticketNO.', 'ticketNO.', 'ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.']
    for index, ticket in enumerate(ticket):
        url_input = "______api______"
        payload = {'verification': '____key___','Part_No': ticket}
        response = requests.request("POST", url, data = payload)
        box.append(response.text.encode('utf8'))
    return box
    
 
 ticket_input = ['ticketNO.','ticketNO.', 'ticketNO.', 'ticketNO.', 'ticketNO.', 'ticketNO.', 'ticketNO.', 'ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.','ticketNO.']
 
 
 url_input = "______api______"
 
 
 def apitable():
    vp_info = []
    vp_info2 = []
    for i in range(len(ticket_input)):
        y = readapi(ticket_input,url_input)
        df_vp = pd.read_json(y[i])
        vp_info = df_vp.iloc[0] 
        vp_info2.append(vp_info)
    return vp_info2
    
    
 
 def vptable():
    vp_table = pd.DataFrame(columns = ['material_status', 'Inventory_quantity'])
    vp_info2 = apitable()
    for info in vp_info2:  
        for k, v in info.items(): # k:key , v:value  # 限定只有store的資訊, items()會讀取我們要的範圍
            # http://tw.gitbook.net/python/dictionary_items.html : items()
            if k == 'material_status': # == 比較是否相等 ---> true or false
                status = v      # = 賦值
            elif k== 'Inventory_quantity':  # 和if本身不互斥,像sql的case when;if...else...就是互斥
                amount = v
                new_row = {'material_status' : status, 'Inventory_quantity' : amount}
                vp_table = vp_table.append(new_row, ignore_index= True)
    return vp_table
    
 
 def vptable2():
    vp_table = vptable()
    dict1 = vp_table['material_status']
    dict2 = vp_table['Inventory_quantity']
    vp_table2 = pd.DataFrame(columns = ['material_status', 'Inventory_quantity'])
    for i in range(0,len(dict1)):
        #for j in range(len(dict2)):
        v1 = dict1[i]['material_status'] 
        v2 = dict2[i]['Inventory_quantity']
        new_row = {'material_status' : v1 , 'Inventory_quantity' : v2}
        vp_table2 = vp_table2.append(new_row, ignore_index= True)
    return vp_table2
    
 
 def dataframeTicketConcat():
    tt = {'ticket':ticket_input}
    ticket_df = pd.DataFrame(tt)
    vp_table2 = vptable2()
    vp_table3 = pd.concat([vp_table2,ticket_df], axis =1, sort=True)
    return vp_table3
    
 
s3 = boto3.client('s3',aws_access_key_id = '____key____',aws_secret_access_key = '_____key_____')
filepath = "vp_table"+"_"+datetime.datetime.now().strftime("%Y-%m-%d")+"_"+datetime.datetime.now().strftime("%H:%M:%S")
bucketName = 'automatingetl'
df = dataframeTicketConcat()
csv_buffer = StringIO()
df.to_csv(csv_buffer)
client = boto3.client('s3')
response = s3.put_object(Body = csv_buffer.getvalue(), Bucket = bucketName, Key = filepath)
print('Put Complete')


import gspread
import os
import gcsfs


dataframe = dataframeTicketConcat()
    

def writeIntoGoogleSheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('___credential___', scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1  # Open the spreadhseet 
    today = time.strftime("%c")
    # 寫入整個dataframe
    writeIntoData = sheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
    return writeIntoData
        
writeIntoGoogleSheet('___sheet_name___')
print('ok1')


