#!/usr/bin/python3
import webbrowser

import PySimpleGUI as sg
from geopy.geocoders import Nominatim

def main():
    # pop-up user input
    location = sg.popup_get_text('Enter your desired destination')
    sg.popup('Destination --->', location)
    
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")

        # entering the location name
    getLoc = loc.geocode(location)
    
        # printing address
    print(getLoc.address)    
    
        # printing latitude and longitude
    print("Latitude = ", getLoc.latitude)
    print("Longitude = ", getLoc.longitude, "\n")
    
        ## user defined info
    lon = (getLoc.longitude)
    lat = (getLoc.latitude)

    userinput = (f"ll={lat},{lon}&z=1000")
    userinput1 = (f"{lat}&lon={lon}")

    WazeAPI = ('https://waze.com/ul?' + userinput)
    Weather = ('https://forecast.weather.gov/MapClick.php?lat=' + userinput1)
    
    print(WazeAPI)
    print(Weather)

    webbrowser.open(WazeAPI)
    webbrowser.open(Weather)

if __name__ == "__main__":
    main()
