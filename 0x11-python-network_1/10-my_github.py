#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]

	url = "https://api.github.com/user"
	response = requests.get(url, auth=HTTPBasicAuth(username, password))

	try:
		json_response = response.json()
		print(json_response.get("id"))
	except ValueError:
		print("Not a valid JSON")
