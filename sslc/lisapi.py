import os
import json 
import requests
import pprint


print_dat = pprint.PrettyPrinter(indent=6)
api_url= "https://api.ssllabs.com/api/v3/analyze?host=tvsmotor.com&publish=off" 

response = requests.get(api_url)

if response.status_code == 200:
    res = response.json()
    print_dat.pprint(res)
    print(len(res))
    # print(res['status'])
    if res['status'] == "DNS":
        print(res['statusMessage'])
        response = requests.get(api_url)
        print("refreshing......")
        print(res['statusMessage'])
        pass
    elif res['status'] == "IN_PROGRESS":
        print("this is in progress phase")
        print(res['endpoints'][0]['statusMessage'])
        pass
    elif res['status'] == "READY":
        print("THIS IS ready phase")
        print(res['endpoints'][0]['statusMessage'])
        print("THE HOST HELATH IS:  " + res['endpoints'][0]['grade'])
        pass
    elif res['status'] == "ERROR":
        print(res['statusMessage'])
        pass
    else:
        print("nothing doing.....")
