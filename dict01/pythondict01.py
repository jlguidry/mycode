#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""

    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
    
    print(switch)
    
    print(type(switch))

    print( switch["hostname"])
    print( switch["ip"])
    #print( switch["lynx"])
    print( switch.get("lynx"))
    
    switch["lynx"] = 890
    print(switch)

#    del switch["vendor"]

    switch.pop("vendor")
    print(switch)

if __name__ == "__main__":
    main()
