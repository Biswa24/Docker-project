import requests
import json
import os
from flask import current_app as app
from datetime import datetime ,date
from pytz import timezone



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    return


def data_indian():
	try:
		url = "https://api.covid19india.org/data.json"
		response = requests.get(url)
		data = response.json()
		with open('./static/json/time_series.json', 'w') as fp:
		    json.dump(data['cases_time_series'], fp)

		with open('./static/json/statewise.json', 'w') as fp:
		    json.dump(data['statewise'], fp)

		return data
	except Exception as inst:
		print(type(inst))
		print(inst.args)
		print(inst)

def data_global():
	try:
		url = "https://corona.lmao.ninja/v2/all"
		response = requests.get(url)
		data = response.json()
		with open('./static/json/global_data.json', 'w') as fp:
		    json.dump(data, fp)
		return data
	except Exception as inst:
		print(type(inst))
		print(inst.args)
		print(inst)


def generator():
	data_indian()
	data_global()
	return


def timer():
	now_utc = datetime.now(timezone('UTC'))
	date_time = str(now_utc.astimezone(timezone('Asia/Kolkata')))
	tz_India = timezone('Asia/Kolkata')
	datetime_India = datetime.now(tz_India)
	date_format = datetime_India.strftime("%A %d. %B %Y,")
	min = str(int(date_time[14:16]) - int(date_time[14:16])%20)
	if len(min)==1:
		min ='00' 
	lastupdated = str(date_format)+" "+date_time[11:14] + min

	return lastupdated


def data_generaion(paths):
    filename = os.path.join(app.static_folder, 'json', paths)
    with open(filename) as fp:
        data = json.load(fp)
    return data

# timer()
# jprint(data_indian())
# jprint(data_global())
