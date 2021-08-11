import requests
import json
from pprint import pprint
from getpass import getpass
import os
# from dotenv import load_dotenv


user_statepool = []
statepool = []
api_key = os.getenv("USER_API_KEY")
population_list = []
casedensity_list = []

totalcase_list = []
totaldeath_list = []
totalnewcase_list = []
totalnewdeath_list = []

totalvacdistributed_list = []
vacinitiatedratio_list = []
vaccompletedratio_list = []


url = f"https://api.covidactnow.org/v2/states.json?apiKey=6a98cc92b3324c62aef26c681936f73c"
response = requests.get(url)
parsed_response = json.loads(response.text)

# append states to the list
for state in parsed_response:
    statepool.append(state["state"])
    population_list.append(state["population"])
    casedensity_list.append(state["metrics"]["caseDensity"])

    totalcase_list.append(state["actuals"]["cases"])
    totaldeath_list.append(state["actuals"]["deaths"])
    totalnewcase_list.append(state["actuals"]["newCases"])
    totalnewdeath_list.append(state["actuals"]["newDeaths"])

    totalvacdistributed_list.append(state["actuals"]["vaccinesDistributed"])
    vacinitiatedratio_list.append(state["metrics"]["vaccinationsInitiatedRatio"])
    vaccompletedratio_list.append(state["metrics"]["vaccinationsCompletedRatio"])



# sort list
population_listsort = sorted(population_list,reverse = True)
casedensity_listsort = sorted(casedensity_list,reverse = True)

totalcase_listsort = sorted(totalcase_list,reverse = True)
totalnewcase_listsort = sorted(totalnewcase_list, reverse = True)
totaldeath_listsort = sorted(totaldeath_list,reverse = True)
totalnewdeath_listsort = sorted(totalnewdeath_list,reverse = True)

totalvacdistributed_listsort = sorted(totalvacdistributed_list, reverse = True)
vacinitiatedratio_listsort = sorted(vacinitiatedratio_list,reverse = True)
vaccompletedratio_listsort = sorted(vaccompletedratio_list, reverse = True)

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
  print("State population:",parsed_response[state_order]["population"],"(Rank",population_listsort.index             (parsed_response[state_order]["population"])+1,"in the US)")

  print("The case density in",selected_state,"is:",parsed_response[state_order]["metrics"]["caseDensity"],"(Rank",casedensity_listsort.index(parsed_response[state_order]["metrics"]["caseDensity"])+1,"in the US)")

  print("-----------------------CASE & DEATH-----------------------")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["cases"],"total cases","(Rank",totalcase_listsort.index(parsed_response[state_order]["actuals"]["cases"])+1,"in the US)")

  print(selected_state,"has",parsed_response[state_order]["actuals"]["deaths"],"total death","(Rank",totaldeath_listsort.index(parsed_response[state_order]["actuals"]["deaths"])+1,"in the US)")

  print(selected_state,"has",parsed_response[state_order]["actuals"]["newCases"],"new cases","(Rank",totalnewcase_listsort.index(parsed_response[state_order]["actuals"]["newCases"])+1,"in the US)")

  print(selected_state,"has",parsed_response[state_order]["actuals"]["newDeaths"],"new deaths","(Rank",totalnewdeath_listsort.index(parsed_response[state_order]["actuals"]["newDeaths"])+1,"in the US)")
  print("-------------------------VACCINES-------------------------")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["vaccinesDistributed"],"total vaccine distributed","(Rank",totalvacdistributed_listsort.index(parsed_response[state_order]["actuals"]["vaccinesDistributed"])+1,"in the US)")

  print("The vaccination initiated ratio is:",parsed_response[state_order]["metrics"]["vaccinationsInitiatedRatio"],"(Rank",vacinitiatedratio_listsort.index(parsed_response[state_order]["metrics"]["vaccinationsInitiatedRatio"])+1,"in the US)")
  
  print("The vaccination completed ratio is:",parsed_response[state_order]["metrics"]["vaccinationsCompletedRatio"],"(Rank",vaccompletedratio_listsort.index(parsed_response[state_order]["metrics"]["vaccinationsCompletedRatio"])+1,"in the US)")

  print("----------------------ICU Information---------------------")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["icuBeds"]["capacity"],"total ICU beds")
  print(selected_state,"has",parsed_response[state_order]["actuals"]["icuBeds"]["currentUsageTotal"],"ICU beds in current use")
  print("The ratio of ICU beds currently in use is:",parsed_response[state_order]["metrics"]["icuCapacityRatio"])
  print(selected_state,"has",parsed_response[state_order]["metrics"]["icuHeadroomDetails"]["currentIcuCovid"],"COVID patients in ICU")
  print(selected_state,"has",parsed_response[state_order]["metrics"]["icuHeadroomDetails"]["currentIcuNonCovid"],"non-COVID patients in ICU")
  print("-----------------------------------------------------------\n\n\n\n\n")