import urllib.request
import json

while True:
    city = input("\Which city's weathervane do you need? (q=quit)")

    if city == "q":
        print("Bye")
        break

    city = city.strip().replace(" ", "+")
    display_city = city.replace("+", " ")
    url = "https://wttr.in/" + city + "?format=j1"


    try:
         response = urllib.request.urlopen(url)
         data = json.loads(response.read())
         temp = data["current_condition"][0]["temp_C"]
         feels_like = data["current_condition"][0]["FeelsLikeC"]
         desc = data["current_condition"][0]["weatherDesc"][0]["value"]

         print("=======" + display_city + " Weather========")
         print("Temp   : " + temp + "C")
         print("Feel_like   : " + feels_like + "C")
         print("Condition  :" + desc)

    except:
        print("Error : Wrong city enter! Please enter Valid city")
    
