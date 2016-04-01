#!/usr/bin/python3

import requests
import json
import time

# Function to make an API call to VirustTotal.  Takes a hash as a parameter.
def virustotalcall(hash):
	url = 'https://www.virustotal.com/vtapi/v2/file/report'
	key = '<INSERT YOUR VIRUSTTOTAL API KEY HERE>'
	parameters = {'resource': hash, 'apikey': key}

	# Requests package is required for this to work.
	response = requests.post(url, data = parameters)
	return response
	
# Open the text file of hashes, read in the file, and assign the contents into a newline-delimited list
hashfile = open('unrulyhashes.txt', 'r').read().split('\n')

for i in hashfile:
	r = virustotalcall(i)
	x = r.json()
	scans = x["scans"]
	
	print("------------------------------------------------------")
	print("")
	print("For hash: " + i)
	
	for scan in scans.keys():
		if scans[scan]["detected"] == True:
			print("  " + scan + " detected this hash as: " + scans[scan]["result"])
		
	print("")
	print("A link to the VirusTotal report for this hash can be found here: " + x["permalink"])
	print("")
	time.sleep(15)
