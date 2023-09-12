#print("Github Users")

import requests
import json
import os

if not os.path.exists("json_files"):
	os.mkdir("json_files")

access_point = "https://api.github.com"
#print (access_point)

response_text = requests.get(access_point + "/rate_limit").text

#json.loads is necessary for reading the file correctly
print(json.loads(response_text))

user_id = "erinata"
response_text = requests.get(access_point + "/users/" + user_id).text

json_text = json.loads(response_text)

#we open the door into the file, we have some json text, we use json.dumps to make it into a format that can be written into a file, 
#then we close the door to the file
#want to save inside json_files folder
file_name = "json_files/" + user_id + ".json"
f = open(file_name, "w")
f.write(json.dumps(json_text))
f.close()