# final_project

Help you search for covid related information state level
# Sample Output on web
State Code:CA

--------------------Basic Information---------------------
['Date:', '2021-08-12']
['State:', 'CA']
['State population:', 39512223, '(Rank', 1, 'in the US']
['The case density in', 'CA', 'is:', 30.6, '(Rank', 23, 'in the US)']
-----------------------CASE & DEATH-----------------------
['CA', 'has', 4168517, 'total cases', '(Rank', 1, 'in the US)']
['CA', 'has', 64838, 'total death', '(Rank', 1, 'in the US)']
['CA', 'has', 11479, 'new cases', '(Rank', 3, 'in the US)']
['CA', 'has', 51, 'new deaths', '(Rank', 4, 'in the US)']
-------------------------VACCINES-------------------------
['CA', 'has', 51879625, 'total vaccine distributed', '(Rank', 1, 'in the US)']
['The vaccination initiated ratio is:', 0.663, '(Rank', 11, 'in the US)']
['The vaccination completed ratio is:', 0.538, '(Rank', 19, 'in the US)']
----------------------ICU Information---------------------
['CA', 'has', 7027, 'total ICU beds', '(Rank', 1, 'in the US)']
['CA', 'has', 5293, 'ICU beds in current use', '(Rank', 3, 'in the US)']
['The ratio of ICU beds currently in use is:', 0.75, '(Rank', 22, 'in the US)']
['CA', 'has', 1227, 'COVID patients in ICU', '(Rank', 3, 'in the US)']
['CA', 'has', 4066, 'non-COVID patients in ICU', '(Rank', 1, 'in the US)']



## Installation

Fork [this repo](https://github.com/liqiansheng/final_project/), then clone or download the forked repo onto your local computer (for example to the Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/final_project/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "covid-env":

```sh
conda create -n covid-env python=3.8
conda activate covid-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

You need to apply for your onw api key on: https://covidactnow.org/data-api

```sh
# these are example contents for the ".env" file:

# required vars:
USER_API_KEY



## Usage

```sh
python -m app.covid_lookup.py
```


# Run app on local 


# MAC OS
```sh
FLASK_APP=web_app flask run
```
There are links with abbreviation info and data definition to give you a better experience

## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server and schedule the server to send you the weather forecast email every day.

## [License](/LICENSE.md)
