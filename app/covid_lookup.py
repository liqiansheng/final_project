import requests
import json
from pprint import pprint
from getpass import getpass
import os
from dotenv import load_dotenv

def get_covid_case(user_input):
 

  load_dotenv()
  user_statepool = []
  statepool = []
  api_key = os.getenv("USER_API_KEY")

  # List for ranking
  population_list = []
  casedensity_list = []

  totalcase_list = []
  totaldeath_list = []
  totalnewcase_list = []
  totalnewdeath_list = []

  totalvacdistributed_list = []
  vacinitiatedratio_list = []
  vaccompletedratio_list = []

  totalicubed_list = []
  icubeduse_list = []
  icubedratio_list = []
  covidicu_list = []
  noncovidicu_list = []


  url = f"https://api.covidactnow.org/v2/states.json?apiKey={api_key}"
  response = requests.get(url)
  parsed_response = json.loads(response.text)
  del parsed_response[25]

  # append states and other variables to the list
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

      totalicubed_list.append(state["actuals"]["icuBeds"]["capacity"])
      icubeduse_list.append(state["actuals"]["icuBeds"]["currentUsageTotal"])
      icubedratio_list.append(state["metrics"]["icuCapacityRatio"])
      covidicu_list.append(state["metrics"]["icuHeadroomDetails"]["currentIcuCovid"])
      noncovidicu_list.append(state["metrics"]["icuHeadroomDetails"]["currentIcuNonCovid"])

  population_listsort = sorted(population_list,reverse = True)
  casedensity_listsort = sorted(casedensity_list,reverse = True)

  totalcase_listsort = sorted(totalcase_list,reverse = True)
  totalnewcase_listsort = sorted(totalnewcase_list, reverse = True)
  totaldeath_listsort = sorted(totaldeath_list,reverse = True)
  totalnewdeath_listsort = sorted(totalnewdeath_list,reverse = True)

  totalvacdistributed_listsort = sorted(totalvacdistributed_list, reverse = True)
  vacinitiatedratio_listsort = sorted(vacinitiatedratio_list,reverse = True)
  vaccompletedratio_listsort = sorted(vaccompletedratio_list, reverse = True)

  totalicubed_listsort = sorted(totalicubed_list, reverse = True)
  icubeduse_listsort = sorted(icubeduse_list,reverse = True)
  icubedratio_listsort = sorted(icubedratio_list, reverse = True)
  covidicu_listsort = sorted(covidicu_list, reverse = True)
  noncovidicu_listsort = sorted(noncovidicu_list, reverse = True)

  # Confirm states

  selected_state = user_input.upper()
  a = "--------------------Basic Information---------------------"
  state_order = statepool.index(selected_state) 
  b = ["Date:", parsed_response[state_order]["lastUpdatedDate"]]
  
  c = ["State:",selected_state]
  d = ["State population:",parsed_response[state_order]["population"],"(Rank",population_listsort.index(parsed_response[state_order]["population"])+1,"in the US"]
  
  e = ["The case density in",selected_state,"is:",parsed_response[state_order]["metrics"]["caseDensity"],"(Rank",casedensity_listsort.index(parsed_response[state_order]["metrics"]["caseDensity"])+1,"in the US)"]

  f = "-----------------------CASE & DEATH-----------------------"
  g = [selected_state,"has",parsed_response[state_order]["actuals"]["cases"],"total cases","(Rank",totalcase_listsort.index(parsed_response[state_order]["actuals"]["cases"])+1,"in the US)"]

  h = [selected_state,"has",parsed_response[state_order]["actuals"]["deaths"],"total death","(Rank",totaldeath_listsort.index(parsed_response[state_order]["actuals"]["deaths"])+1,"in the US)"]

  i = [selected_state,"has",parsed_response[state_order]["actuals"]["newCases"],"new cases","(Rank",totalnewcase_listsort.index(parsed_response[state_order]["actuals"]["newCases"])+1,"in the US)"]

  j = [selected_state,"has",parsed_response[state_order]["actuals"]["newDeaths"],"new deaths","(Rank",totalnewdeath_listsort.index(parsed_response[state_order]["actuals"]["newDeaths"])+1,"in the US)"]
  k = "-------------------------VACCINES-------------------------"
  l = [selected_state,"has",parsed_response[state_order]["actuals"]["vaccinesDistributed"],"total vaccine distributed","(Rank",totalvacdistributed_listsort.index(parsed_response[state_order]["actuals"]["vaccinesDistributed"])+1,"in the US)"]

  m = ["The vaccination initiated ratio is:",parsed_response[state_order]["metrics"]["vaccinationsInitiatedRatio"],"(Rank",vacinitiatedratio_listsort.index(parsed_response[state_order]["metrics"]["vaccinationsInitiatedRatio"])+1,"in the US)"]
  
  n = ["The vaccination completed ratio is:",parsed_response[state_order]["metrics"]["vaccinationsCompletedRatio"],"(Rank",vaccompletedratio_listsort.index(parsed_response[state_order]["metrics"]["vaccinationsCompletedRatio"])+1,"in the US)"]

  o = "----------------------ICU Information---------------------"
  p = [selected_state,"has",parsed_response[state_order]["actuals"]["icuBeds"]["capacity"],"total ICU beds","(Rank",totalicubed_listsort.index(parsed_response[state_order]["actuals"]["icuBeds"]["capacity"])+1,"in the US)"]

  q = [selected_state,"has",parsed_response[state_order]["actuals"]["icuBeds"]["currentUsageTotal"],"ICU beds in current use","(Rank",icubeduse_listsort.index(parsed_response[state_order]["actuals"]["icuBeds"]["currentUsageTotal"])+1,"in the US)"]

  r = ["The ratio of ICU beds currently in use is:",parsed_response[state_order]["metrics"]["icuCapacityRatio"],"(Rank",icubedratio_listsort.index(parsed_response[state_order]["metrics"]["icuCapacityRatio"])+1,"in the US)"]

  s = [selected_state,"has",parsed_response[state_order]["metrics"]["icuHeadroomDetails"]["currentIcuCovid"],"COVID patients in ICU","(Rank",covidicu_listsort.index(parsed_response[state_order]["metrics"]["icuHeadroomDetails"]["currentIcuCovid"])+1,"in the US)"]

  t = [selected_state,"has",parsed_response[state_order]["metrics"]["icuHeadroomDetails"]["currentIcuNonCovid"],"non-COVID patients in ICU","(Rank",noncovidicu_listsort.index(parsed_response[state_order]["metrics"]["icuHeadroomDetails"]["currentIcuNonCovid"])+1,"in the US)"]

  u = "-----------------------------------------------------------\n\n\n\n\n"
  covid_case = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u]
  return covid_case
  