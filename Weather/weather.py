#Copyright 2015 All Rights Reserved. Tallulah Falls Computer Science. GPLv2
#This source file is free software, under the terms of the GNU GPLv2 General Public License.
import json
import urllib.request
import os
import sys
# Create and format API URL
API_KEY = open('API_KEY.txt', encoding="utf-8").read() # Paste API KEY in text file within this directory.
if '<insert your api key here>' in API_KEY:
    print ('ERROR: Place your api key in the "API_KEY.txt" file')
    sys.exit()

# Clears the console and prints header
def printHeader():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n                _\n              (`  ).                   _\n             (     ).              .:(`  )`.\n)           _(       '`.          :(   .    )\n        .=(`(      .   )     .--  `.  (    ) )\n       ((    (..__.:'-'   .+(   )   ` _`  ) )\n`.     `(       ) )       (   .  )     (   )  ._\n  )      ` __.:'   )     (   (   ))     `-'.-(`  )\n)  )  ( )       --'       `- __.'         :(      ))\n.-'  (_.'          .')                    `(    )  ))\n                  (_  )                     ` __.:'\n\n--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.------.")
    print ("|====================================================================")
    print ("|TFS COMPUTER SCIENCE PYTHON WEATHER APP v0.1.0")
    print ("|====================================================================")
printHeader()# execute

# Get the user's zip code.
zip = (input("|Enter Your Zip Code: "))

# JSON Fetch and Parser
apiURL = 'http://api.wunderground.com/api/' + API_KEY + '/geolookup/conditions/q/' + zip + '.json' # apiURL Builder
with urllib.request.urlopen(apiURL) as url:
    response = url.read()
charset = url.info(). get_content_charset('utf-8')  # UTF-8 Encode
json_string = json.loads(response.decode(charset))
parsed_json = json_string

# Check for an invalid zip code input
if 'No cities match your search query' in str(response):
    print ('ERROR: INVALID ZIP')
    sys.exit()

# Parsed Variables (Temp, Humidity, Conditions)
locationCity = str(parsed_json['location']['city'])
locationState = str(parsed_json['location']['state'])
weather = str(parsed_json['current_observation']['weather'])
wTemp = str(parsed_json['current_observation']['temperature_string'])
wFeelsLikeTemp = str(parsed_json['current_observation']['feelslike_string'])
wRelativeHumidity = str(parsed_json['current_observation']['relative_humidity'])
wPressure = str(parsed_json['current_observation']['pressure_in'])

# Output
printHeader()
print ('|Weather For: ' + locationCity + ' ' + locationState )
print ("|====================================================================")
print ('|Weather: ' + weather)
print ('|Temperature: ' + wTemp)
print ('|Feels Like: ' + wFeelsLikeTemp)
print ('|Humidity: ' + wRelativeHumidity)
print ('|Pressure: ' + wPressure)




