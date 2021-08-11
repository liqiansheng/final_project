import requests
import json
from pprint import pprint
from getpass import getpass
import os
# from dotenv import load_dotenv


user_statepool = []
statepool = []
api_key = os.getenv("USER_API_KEY")


url = f"https://api.covidactnow.org/v2/states.json?apiKey=6a98cc92b3324c62aef26c681936f73c"
response = requests.get(url)
parsed_response = json.loads(response.text)
print(parsed_response[25])
print(parsed_response[0].keys())
print(parsed_response[25]["state"])
print(type(parsed_response[0]["state"]))

# append states to the list
for state in parsed_response:
  statepool.append(state["state"])

# ask user for the states
while True:
  user_input = input("Please name a state you are interested in. Enter 'Done' to skip.")
  if user_input.upper() == "DONE":
    break
  elif user_input.upper() not in statepool:
    print("Please enter a valid state abbreviation. If you are not sure, please go to the 'Abbrevation' page.")
  else:
    user_statepool.append(user_input.upper())