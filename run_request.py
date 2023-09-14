#print("Github Users")

import requests
import json
import os
import pandas
import time
#pandas to read csv file, time to help the server

#create a folder for the output
if not os.path.exists("json_files"):
	os.mkdir("json_files")

access_point = "https://api.github.com"
#print (access_point)

#read the token file
f = open("token", "r")
token = f.read()
f.close

#have pandas read the csv file
#get a specific column from the data
id_list = pandas.read_csv("seed.csv")
id_list = id_list['ghid']

#so we don't have a small limit of requests, set up github session, sign in with username in token
github_session = requests.Session()
github_session.auth = ("hannahmisurati", token)

#set up for loop to have code read seed.csv file and run code for all users
#we open the door into the file, we have some json text, we use json.dumps to make it into a format that can be written into a file, 
#then we close the door to the file
#want to save inside json_files folder, see line 26
#json.loads is necessary for reading the file correctly


response_text = github_session.get(access_point + "/rate_limit").text
print(json.loads(response_text))

for user_id in id_list:
	file_name = "json_files/" + user_id + ".json"

	if os.path.exists(file_name):
		#pass
		print("File exists: ", user_id)
	else: 

		try:

			print(user_id)
			response_text = github_session.get(access_point + "/users/" + user_id).text
			json_text = json.loads(response_text)


	#name the file a tmp file while the code is running and change after code is complete, in case of server failure
			f = open(file_name + ".tmp", "w")
			f.write(json.dumps(json_text))
			f.close()
			os.rename(file_name + ".tmp", file_name)

		except Exception as e:
			print(e)
			
		time.sleep(5)



