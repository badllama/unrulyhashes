#!/usr/bin/python3

import requests
import json
import time
from flask import render_template
from flask import request
from flask import Flask,send_from_directory
app = Flask(__name__)

# Function to make an API call to VirustTotal.  Takes a hash as a parameter.
def virustotalcall(hash):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        key = 'INSERT VIRUSTOTAL API KEY HERE'
        parameters = {'resource': hash, 'apikey': key}

        # Requests package is required for this to work.
        response = requests.post(url, data = parameters)
        return response

# REMOVED and replaced by user-supplied text field -- Open the text file of hashes, read in the file, and assign the contents into a newline-delimited list
#hashfile = open('unrulyhashes.txt', 'r').read().split('\n')

@app.route("/lookup", methods=['POST'])
def lookup():
        hashinput = request.form['hashes']
        hashfile = hashinput.splitlines()
        browserString = ''
        for i in hashfile:
                r = virustotalcall(i)
                x = r.json()
                scans = x["scans"]

                print("Working on..." + i)
                browserString += "<br><br>Hash: " + i
                for scan in scans.keys():
                        if scans[scan]["detected"] == True:
                                print(str(scan))
                                browserString += "<br>  " + str(scan) + " detected this hash as: " + str(scans[scan]["result"])
                time.sleep(15)
        return browserString

@app.route("/")
@app.route("/index.html")
def index():
        return send_from_directory('static', "input.html")
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

