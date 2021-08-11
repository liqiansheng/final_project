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

# Confirm states
for user_state in user_statepool:
  print("You chose:",user_state)


# Output
for selected_state in user_statepool:
  print("--------------------Basic Information---------------------")
  state_order = statepool.index(selected_state) 
  print("Date:",parsed_response[state_order]["lastUpdatedDate"])
  print("State:",selected_state)
  print("State population:",parsed_response[state_order]["population"])
  print("The case density in",selected_state,"is:",parsed_response[state_order]["metrics"]["caseDensity"])
  print("-----------------------CASE & DEATH-----------------------")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["cases"],"total cases")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["deaths"],"total death")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["newCases"],"new cases")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["newDeaths"],"new deaths")
  print("-------------------------VACCINES-------------------------")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["vaccinesDistributed"],"total vaccine distributed")
  print("The vaccination initiated ratio is:",parsed_response[state_order]["metrics"]["vaccinationsInitiatedRatio"])
  print("The vaccination initiated ratio is:",parsed_response[state_order]["metrics"]["vaccinationsCompletedRatio"])
  print("----------------------ICU Information---------------------")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["icuBeds"]["capacity"],"total ICU beds")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["icuBeds"]["currentUsageTotal"],"ICU beds in current use")
  print("The ratio of ICU beds currently in use is:",parsed_response[state_order]["metrics"]["icuCapacityRatio"])
  print(selected_state,"has",parsed_response[state_order]["metrics"]["icuHeadroomDetails"]["currentIcuCovid"],"COVID patients in ICU")
  print(selected_state,"has",parsed_response[state_order]["metrics"]["icuHeadroomDetails"]["currentIcuNonCovid"],"non-COVID patients in ICU")
  print("-----------------------------------------------------------\n\n\n\n\n")