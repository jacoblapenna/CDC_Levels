# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:15:55 2022

@author: jlapenna
"""

from requests import get
import pickle
from datetime import datetime

API_KEY = "3dc70dc41673495bb8e35441d31d1142"

data = get(f"https://api.covidactnow.org/v2/counties.json?apiKey={API_KEY}")

data_dict = data.json()

time_str = datetime.now().strftime("%m%d%Y%H%M%S")
with open(f"data_{time_str}.pickle", "wb") as f:
    pickle.dump(data_dict, f)


"""
# Geopandas to map plot stuff
https://medium.com/analytics-vidhya/making-colored-country-maps-with-real-data-using-matplotlib-and-geopandas-2d10687ca7ac
https://jcutrer.com/python/learn-geopandas-plotting-usmaps

# send email notifications
https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server

# Definitions
data_dict[position]["communityLevels"]["cdcCommunityLevel"]
Possible values: - 0: Low - 1: Moderate - 2: Substantial - 3: High - 4: Unknown
From observation on CDC's map:
0 = Low (green)
1 = Medium (yellow)
2,3 = High (orange/red)

https://covid.cdc.gov/covid-data-tracker/#cases_casesper100klast7days

"""

# with open("data_09012022142926.pickle", 'rb') as f:
#     data_dict_old = pickle.load(f)

# checker
# for i, county in enumerate(data_dict):
#     old_county = data_dict_old[i]
#     new_level = county["communityLevels"]["cdcCommunityLevel"]
#     old_level = old_county["communityLevels"]["cdcCommunityLevel"]
#     if county["fips"] != old_county["fips"]:
#         print(i, (county["fips"], old_county["fips"]))
#     if new_level != old_level:
#         print(i, new_level, old_level)
