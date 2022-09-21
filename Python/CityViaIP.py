# This script gets the city of the user via their ip address

import requests

# Get the ip address of the user
ip_address = requests.get('https://api.ipify.org').text

# Get the city of the user
city = requests.get('https://ipapi.co/' + ip_address + '/city/').text

# Print the city of the user
print("You are in " + city)

# Output
# You are in New York
