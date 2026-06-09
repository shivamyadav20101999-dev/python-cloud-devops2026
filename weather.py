import urllib.request
import json

city = input("Which city's weathervane do you need?");
city = city.strip().replace(" ", "+")
url = "https://wttr.in/" + city + "?format=j1"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    temp = data["current_condition"][0]["temp_C"]
    feels_like = data["current_condition"][0]["FeelsLikeC"]
    desc = data["current_condition"][0]["weatherDesc"][0]["value"]

    print("==== " + city + "  Weather ====")
    print("Temp     : " + temp + "C")
    print("Feels    : " + feels_like + "C")
    print("Condition: " + desc)

except:
    print("Error " + city + "Wrong city enter, please enter valid city name")
