import requests

# Import 
import json

controller='sandboxdnac.cisco.com'

def getTicket():
	
	url = "https://" + controller + "/api/v1/ticket"

	# The username and password to access the DNA Center
	payload = {"username":"devnetuser","password":"Cisco123!"}

	# Content type must be included in the header
	header = {"content-type": "application/json"}

	# Perform a POST on the specified url to get the token
	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

	# Convert response to JSON format
	res_json=response.json()

	# Parse the JSON to get the token
	ticket = res_json["response"]["serviceTicket"]

	return ticket

getTicket()

