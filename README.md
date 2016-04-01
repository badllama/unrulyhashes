# unrulyhashes
A python program that uses flask to allow users to query VirusTotal for malware hash analysis.

For the python program to run it also requires a /static directory to be in the same location as the file, and an input.html file stored in that static directory.  

# unrulyhashes-cli.py
A command-line variant of the unrulyhashes program which takes in a text file of hashes and programmatically submits them to VirusTotal for analysis.

To use of the script:
* update line 10 and replace '<INSERT YOUR VIRUSTTOTAL API KEY HERE>' with your own API key (the ' should remain afterwards).
* place a file called 'unrulyhashes.txt' in the same location as the python script.  
* put as many hashes as you like in the text file, but only put one hash per line.


