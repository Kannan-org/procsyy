from pycrtsh import Crtsh
import pprint
import datetime
import os
import requests
import json
import subprocess
# c = Crtsh()
# print_dat = pprint.PrettyPrinter(indent=6)
# dom = input("enter domain you wish :  ")
# certs = c.search(dom)

# details = c.get(certs[0]["id"], type="id")
# print_dat = pprint.PrettyPrinter(indent=6)
# # print_dat.pprint(details)

# print("\n------------------------------------------------------------------\n")

# print_dat.pprint(details.get('subject'))

# print("\n------------------------------------------------------------------\n")

# print_dat.pprint(details['extensions']['authority_information_access'])

# print("\n------------------------------------------------------------------\n")
# not_b4 = details['not_before']
# not_after = details['not_after']
# print("Not Before thsi date: " + not_b4.strftime('%d-%m-%Y %H:%M'))

# print("NOT After this date: " + not_after.strftime('%d-%m-%Y %H:%M'))

# print("\n------------------------------------------------------------------\n")
# pubk = details.get('publickey')

# print_dat.pprint("Algorithm: " + pubk['algorithm'])
# print_dat.pprint("SHA256: " + pubk['sha256'])
# print_dat.pprint("Size:  " + str(pubk['size']))

# print("\n------------------------------------------------------------------\n")

# print_dat.pprint(details.get('issuer'))

print("\n------------------------------------------------------------------\n")
# ssllab = "python3 ./python-ssllabs/ssllabs-cli.py {} |jq \".endpoints[] | [.grade]\""
res = subprocess.getoutput(['python3 ./python-ssllabs/ssllabs-cli.py tvsmotor.com |jq \".endpoints[] | [.grade]\"'])
print(res[5])
print("\n------------------------------------------------------------------\n")

# loduku pandi, nai sekar, oteri nari, saniya sakeda, patasu balu, masoor ali khan,madasamy, adhivasi,
# killer pandi , banner ji
# vavaal, 23 pulikesi, amavasai, soona paanan, setup chellapa, nesamani, bomb pakri,  
# pichumani, soosai, theepori thirumugam, sundi motharam, dhandapani, krirkalan, body soda, samarasam, digil pandi, padithurai pandi
# snake babu, enconter ekambaram, seeripula, vandu murugan.







