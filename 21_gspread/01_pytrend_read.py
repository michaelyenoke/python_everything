import gspread
import pandas as pd
import numpy as np
import json
import csv
import matplotlib.pyplot as plt
import heapq
import os
import gcsfs
import warnings 
import schedule
import time
import boto3
from io import StringIO # python3; python2: BytesIO 
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from pytrends.request import TrendReq
from time import sleep
from numpy.random import randn
from datetime import datetime, timedelta
from pytz import timezone


def getGoogleSheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1  # Open the spreadhseet
    data  = sheet.get_all_values()  # Get a list of all records- dictionary # sheet.get_all_values() 
    return data
    

getGoogleSheet('pysheet7')
