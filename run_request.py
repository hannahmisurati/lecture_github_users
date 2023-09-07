print("Github Users")

import requests
import json

access_point = "https://api.github.com"
print (access_point)

response_text = requests.get(access_point + "/rate_limit").text

print(json.loads(response_text))
