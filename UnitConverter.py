#Adjust the units of the finished categories so they have a space

def area_conversion():
    pass

def capacity_conversion():
    units = ["Kilolitre - Hectolitre", "Kilolitre - Decalitre", "Kilolitre - Litre", "Kilolitre - Decilitre", "Kilolitre - Centilitre", "Kilolitre - Millilitre", "Hectolitre - Kilolitre", "Hectolitre - Decalitre", "Hectolitre - Litre", "Hectolitre - Decilitre", "Hectolitre - Centilitre", "Hectolitre - Millilitre", "Decalitre - Kilolitre", "Decalitre - Hectolitre", "Decalitre - Litre", "Decalitre - Decilitre", "Decalitre - Centilitre", "Decalitre - Millilitre", "Litre - Kilolitre", "Litre - Hectolitre", "Litre - Decalitre", "Litre - Decilitre", "Litre - Centilitre", "Litre - Millilitre", "Decilitre - Kilolitre", "Decilitre - Hectolitre", "Decilitre - Decalitre", "Decilitre - Litre", "Decilitre - Centilitre", "Decilitre - Millilitre", "Centilitre - Kilolitre", "Centilitre - Hectolitre", "Centilitre - Decalitre", "Centilitre - Litre", "Centilitre - Decilitre", "Centilitre - Millilitre", "Millitre - Kilolitre", "Millitre - Hectolitre", "Millitre - Decalitre", "Millitre - Litre", "Millitre - Decilitre", "Millitre - Centilitre"]
    print("Select Capacity Conversion".upper())
    for i, value in enumerate(units, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1 or response == 2 or response == 3 or response == 4 or response == 5 or response == 6:
                v1 = float(input("Enter Kilolitre Value: ".upper()))
                if response == 1:
                    ans1 = v1 * 10
                    print(f"{v1} kl is equal to {ans1} hl.")
                elif response == 2:
                    ans2 = v1 * 100
                    print(f"{v1} kl is equal to {ans2} dl.")
                elif response == 3:
                    ans3 = v1 * 1000
                    print(f"{v1} kl is equal to {ans3} l.")
                elif response == 4:
                    ans4 = v1 * 10000
                    print(f"{v1} kl is equal to {ans4} dl.")
                elif response == 5:
                    ans5 = v1 * 100000
                    print(f"{v1} kl is equal to {ans5} cl.")
                elif response == 6:
                    ans6 = v1 * 1000000
                    print(f"{v1} kl is equal to {ans6} ml.")
                break
            elif response == 7 or response == 8 or response == 9 or response == 10 or response == 11 or response == 12:
                v2 = float(input("Enter Hectolitre Value: ".upper()))
                if response == 7:
                    ans7 = v2 * 0.1
                    print(f"{v2} hl is equal to {ans7} kl.")
                elif response == 8:
                    ans8 = v2 * 10
                    print(f"{v2} hl is equal to {ans8} dl.")
                elif response == 9:
                    ans9 = v2 * 100
                    print(f"{v2} hl is equal to {ans9} l.")
                elif response == 10:
                    ans10 = v2 * 1000
                    print(f"{v2} hl is equal to {ans10} dl.")
                elif response == 11:
                    ans11 = v2 * 10000
                    print(f"{v2} hl is equal to {ans11} cl.")
                elif response == 12:
                    ans12 = v2 * 100000
                    print(f"{v2} hl is equal to {ans12} ml.")
                break
            elif response == 13 or response == 14 or response == 15 or response == 16 or response == 17 or response == 18:
                v3 = float(input("Enter Decalitre Value: ".upper()))
                if response == 13:
                    ans13 = v3 * 0.01
                    print(f"{v3} dl is equal to {ans13} kl.")
                elif response == 14:
                    ans14 = v3 * 0.1
                    print(f"{v3} dl is equal to {ans14} hl.")
                elif response == 15:
                    ans15 = v3 * 10
                    print(f"{v3} dl is equal to {ans15} l.")
                elif response == 16:
                    ans16 = v3 * 100
                    print(f"{v3} dl is equal to {ans16} dl.")
                elif response == 17:
                    ans17 = v3 * 1000
                    print(f"{v3} dl is equal to {ans17} cl.")
                elif response == 18:
                    ans18 = v3 * 10000
                    print(f"{v3} dl is equal to {ans18} ml.")
                break
            elif response == 19 or response == 20 or response == 21 or response == 22 or response == 23 or response == 24:
                v4 = float(input("Enter Litre Value: ".upper()))
                if response == 19:
                    ans19 = v4 * 0.001
                    print(f"{v4} l is equal to {ans19} kl.")
                elif response == 20:
                    ans20 = v4 * 0.01
                    print(f"{v4} l is equal to {ans20} hl.")
                elif response == 21:
                    ans21 = v4 * 0.1
                    print(f"{v4} l is equal to {ans21} dl.")
                elif response == 22:
                    ans22 = v4 * 10
                    print(f"{v4} l is equal to {ans22} dl.")
                elif response == 23:
                    ans23 = v4 * 100
                    print(f"{v4} l is equal to {ans23} cl.")
                elif response == 24:
                    ans24 = v4 * 1000
                    print(f"{v4} l is equal to {ans24} ml.")
                break
            elif response == 25 or response == 26 or response == 27 or response == 28 or response == 29 or response == 30:
                v5 = float(input("Enter Decilitre Value: ".upper()))
                if response == 25:
                    ans25 = v5 * 0.0001
                    print(f"{v5} dl is equal to {ans25} kl.")
                elif response == 26:
                    ans26 = v5 * 0.001
                    print(f"{v5} dl is equal to {ans26} hl.")
                elif response == 27:
                    ans27 = v5 * 0.01
                    print(f"{v5} dl is equal to {ans27} dl.")
                elif response == 28:
                    ans28 = v5 * 0.1
                    print(f"{v5} dl is equal to {ans28} l.")
                elif response == 29:
                    ans29 = v5 * 10
                    print(f"{v5} dl is equal to {ans29} cl.")
                elif response == 30:
                    ans30 = v5 * 100
                    print(f"{v5} dl is equal to {ans30} ml.")
                break
            elif response == 31 or response == 32 or response == 33 or response == 34 or response == 35 or response == 36:
                v6 = float(input("Enter Centilitre Value: ".upper()))
                if response == 31:
                    ans31 = v6 * 0.00001
                    print(f"{v6} cl is equal to {ans31} kl.")
                elif response == 32:
                    ans32 = v6 * 0.0001
                    print(f"{v6} cl is equal to {ans32} hl.")
                elif response == 33:
                    ans33 = v6 * 0.001
                    print(f"{v6} cl is equal to {ans33} dl.")
                elif response == 34:
                    ans34 = v6 * 0.01
                    print(f"{v6} cl is equal to {ans34} l.")
                elif response == 35:
                    ans35 = v6 * 0.1
                    print(f"{v6} cl is equal to {ans35} dl.")
                elif response == 36:
                    ans36 = v6 * 10
                    print(f"{v6} cl is equal to {ans36} ml.")
                break
            elif response == 37 or response == 38 or response == 39 or response == 40 or response == 41 or response == 42:
                v7 = float(input("Enter Millilitre Value: ".upper()))
                if response == 37:
                    ans37 = v7 * 0.000001
                    print(f"{v7} ml is equal to {ans37} kl.")
                elif response == 38:
                    ans38 = v7 * 0.00001
                    print(f"{v7}ml is equal to {ans38} hl.")
                elif response == 39:
                    ans39 = v7 * 0.0001
                    print(f"{v7} ml is equal to {ans39} dl.")
                elif response == 40:
                    ans40 = v7 * 0.001
                    print(f"{v7} ml is equal to {ans40} l.")
                elif response == 41:
                    ans41 = v7 * 0.01
                    print(f"{v7} ml is equal to {ans41} dl.")
                elif response == 42:
                    ans42 = v7 * 0.1
                    print(f"{v7} ml is equal to {ans42} cl.")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")
    
def distance_length_height_conversion():
    pass

def energy_conversion():
    units = ["Joule - Kilojoule", "Joule - Kilowatt hour", "Joule - Watt hour", "Kilojoule - Joule", "Kilojoule - Kilowatt hour", "Kilojoule - Watt hour", "Kilowatt hour - Joule", "Kilowatt hour - Kilojoule", "Kilowatt hour - Watt hour", "Watt hour - Joule", "Watt hour - Kilojoule", "Watt hour - Kilowatt hour"]
    print("Select Energy Conversion".upper())
    for i, value in enumerate(units, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1 or response == 2 or response == 3:
                v1 = float(input("Enter Joule Value: ".upper()))
                if response == 1:
                    ans1 = v1 * 0.001
                    print(f"{v1} J is equal to {ans1} kJ.")
                elif response == 2:
                    ans2 = v1 / 3600000
                    print(f"{v1} J is equal to {ans2} kWh.")
                elif response == 3:
                    ans3 = v1 / 3600
                    print(f"{v1} J is equal to {ans3} Wh.")
                break
            elif response == 4 or response == 5 or response == 6:
                v2 = float(input("Enter Kilojoule Value: ".upper()))
                if response == 4:
                    ans4 = v2 * 1000
                    print(f"{v2} kJ is equal to {ans4} J.")
                elif response == 5:
                    ans5 = v2 / 3600
                    print(f"{v1} kJ is equal to {ans5} kWh.")
                elif response == 6:
                    ans6 = v2 / 3.6
                    print(f"{v1} kJ is equal to {ans6} Wh.")
                break
            elif response == 7 or response == 8 or response == 9:
                v3 = float(input("Enter Kilowatt hour Value: ".upper()))
                if response == 7:
                    ans7 = v3 * 3600000
                    print(f"{v3} kWh is equal to {ans7} J.")
                elif response == 8:
                    ans8 = v3 * 3600
                    print(f"{v3} kWh is equal to {ans8} kJ.")
                elif response == 9:
                    ans9 = v3 * 1000
                    print(f"{v3} kWh is equal to {ans9} Wh.")
                break
            elif response == 10 or response == 11 or response == 12:
                v4 = float(input("Enter Watt hour Value: ".upper()))
                if response == 10:
                    ans10 = v4 * 3600
                    print(f"{v4} Wh is equal to {ans10} J.")
                elif response == 11:
                    ans11 = v4 * 3.6
                    print(f"{v4} Wh is equal to {ans11} kJ.")
                elif response == 12:
                    ans12 = v4 / 3.6
                    print(f"{v4} Wh is equal to {ans12} kWh.")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def frequency_conversion():
    units = ["Hertz - Kilohertz", "Hertz - Megahertz", "Hertz - Gigahertz", "Kilohertz - Hertz", "Kilohertz - Megahertz", "Kilohertz - Gigahertz", "Megahertz - Hertz", "Megahertz - Kilohertz", "Megahertz - Gigahertz", "Gigahertz - Hertz", "Gigahertz - Kilohertz", "Gigahertz - Megahertz"]
    print("Select Frequency Conversion".upper())
    for i, value in enumerate(units, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1 or response == 2 or response == 3:
                v1 = float(input("Enter Hertz Value: "))
                if response == 1:
                    ans1 = v1 * 0.001
                    print(f"{v1} Hz is equal to {ans1} KHz.")
                elif response == 2:
                    ans2 = v1 * 0.000001
                    print(f"{v1} Hz is equal to {ans2} MHz.")
                elif response == 3:
                    ans3 = v1 * 0.000000001
                    print(f"{v1} Hz is equal to {ans3} GHz.")
                break
            elif response == 4 or response == 5 or response == 6:
                v2 = float(input("Enter Kilohertz Value: ".upper()))
                if response == 4:
                    ans4 = v2 * 1000
                    print(f"{v2} KHz is equal to {ans4} Hz.")
                elif response == 5:
                    ans5 = v2 * 0.001
                    print(f"{v2} KHz is equal to {ans5} MHz.")
                elif response == 6:
                    ans6 = v2 * 0.000001
                    print(f"{v2} KHz is equal to {ans6} GHz.")
                break
            elif response == 7 or response == 8 or response == 9:
                v3 = float(input("Enter Megahertz Value: ".upper()))
                if response == 7:
                    ans7 = v3 * 1000000
                    print(f"{v3} MHz is equal to {ans7} Hz.")
                elif response == 8:
                    ans8 = v3 * 1000
                    print(f"{v3} MHz is equal to {ans8} KHz.")
                elif response == 9:
                    ans9 = v3 * 0.001
                    print(f"{v3} MHz is equal to {ans9} GHz.")
                break
            elif response == 10 or response == 11 or response == 12:
                v4 = float(input("Enter Gigahertz Value: ".upper()))
                if response == 10:
                    ans10 = v4 * 1000000000
                    print(f"{v4} GHz is equal to {ans10} Hz.")
                elif response == 11:
                    ans11 = v4 * 1000000
                    print(f"{v4} GHz is equal to {ans11} KHz.")
                elif response == 12:
                    ans12 = v4 * 1000
                    print(f"{v4} MHz is equal to {ans12} GHz.")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def power_conversion():
    pass

def pressure_conversion():
    units = ["Bar - Pascal", "Bar - Standard Atmosphere", "Pascal - Bar", "Pascal - Standard Atmosphere", "Standard Atmosphere - Bar", "Standard Atmosphere - Pascal"]
    print("Select Pressure Conversion".upper())
    for i, value in enumerate(units, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1 or response == 2:
                v1 = float(input("Enter Bar Value: "))
                if response == 1:
                    ans1 = v1 * 100000
                    print(f"{v1} bar is equal to {ans1} Pa.")
                elif response == 2:
                    ans2 = v1 * 0.986923
                    print(f"{v1} bar is equal to {ans2} atm.")
                break
            elif response == 3 or response == 4:
                v2 = float(input("Enter Pascal Value: ".upper()))
                if response == 3:
                    ans3 = v2 / 100000
                    print(f"{v2} Pa is equal to {ans3} bar.")
                elif response == 4:
                    ans4 = v2 / 101325
                    print(f"{v2} Pa is equal to {ans4} atm.")
                break
            elif response == 5 or response == 6:
                v3 = float(input("Enter Standard Atmosphere Value: ".upper()))
                if response == 5:
                    ans5 = v3 * 1.01325
                    print(f"{v3} atm is equal to {ans5} bar.")
                elif response == 6:
                    ans6 = v3 * 101325
                    print(f"{v3} atm is equal to {ans6} Pa")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def speed_conversion():
    units = ["Miles per hour - Metres per second", "Miles per hour - Kilometres per hour", "Metres per second - Miles per hour", "Metres per second - Kilometres per hour", "Kilometres per hour - Miles per hour", "Kilometres per hour - Metres per second"]
    print("Select Speed Conversion".upper())
    for i, value in enumerate(units, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1 or response == 2:
                v1 = float(input("Enter Miles per hour Value: ".upper()))
                if response == 1:
                    ans1 = v1 * 0.44704
                    print(f"{v1} mph is equal to {ans1} m/s.")
                elif response == 2:
                    ans2 = v1 * 1.60934
                    print(f"{v1} mph is equal to {ans2} km/h.")
                break
            elif response == 3 or response == 4:
                v2 = float(input("Enter Metres per second Value: ".upper()))
                if response == 3:
                    ans3 = v2 * 2.23694
                    print(f"{v2} m/s is equal to {ans3} mph.")
                elif response == 4:
                    ans4 = v2 * 3.6
                    print(f"{v2} m/s is equal to {ans4} km/h.")
                break
            elif response == 5 or response == 6:
                v3 = float(input("Enter Kilometre per hour Value: ".upper()))
                if response == 5:
                    ans5 = v3 * 0.621371
                    print(f"{v3} km/h is equal to {ans5} mph.")
                elif response == 6:
                    ans6 = v3 * 0.277778
                    print(f"{v3} km/h is equal to {ans6} m/s.")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def temperature_conversion():
    units = ["Celsius - Fahrenheit", "Celsius - Kelvin", "Fahrenheit - Celsius", "Fahrenheit - Kelvin", "Kelvin - Celsius", "Kelvin - Fahrenheit"]
    print("Select Temperature Conversion".upper())
    for i, value in enumerate(units, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1 or response == 2:
                v1 = float(input("Enter Celsius Value: ".upper()))
                if response == 1:
                    ans1 = (v1 * 1.8) + 32
                    print(f"{v1}°C is equal to {ans1}°F.")
                elif response == 2:
                    ans2 = v1 + 273.15
                    print(f"{v1}°C is equal to {ans2} K.")
                break
            elif response == 3 or response == 4:
                v2 = float(input("Enter Fahrenheit Value: ".upper()))
                if response == 3:
                    ans3 = (v2 - 32) / 1.8
                    print(f"{v2}°F is equal to {ans3}°C.")
                elif response == 4:
                    ans4 = ((v2 - 32) / 1.8) + 273.15
                    print(f"{v2}°F is equal to {ans4} K.")
                break
            elif response == 5 or response == 6:
                v3 = float(input("Enter Kelvin Value: ".upper()))
                if response == 5:
                    ans5 = v3 - 273.15
                    print(f"{v3} K is equal to {ans5}°C.")
                elif response == 6:
                    ans6 = ((v3 - 273.15) * 1.8) + 32
                    print(f"{v3} K is equal to {ans6}°F.")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def time_conversion():
    units = ["Seconds - Minutes", "Seconds - Hours", "Seconds - Days", "Seconds - Weeks", "Seconds - Months", "Seconds - Years", "Minutes - Seconds", "Minutes - Hours", "Minutes - Days", "Minutes - Weeks", "Minutes - Months", "Minutes - Years", "Hours - Seconds", "Hours - Minutes", "Hours - Days", "Hours - Weeks", "Hours - Months", "Hours - Years", "Days - Seconds", "Days - Minutes", "Days - Hours", "Days - Weeks", "Days - Months", "Days - Years", "Weeks - Seconds", "Weeks - Minutes", "Weeks - Hours", "Weeks - Days", "Weeks - Months", "Weeks - Years", "Months - Seconds", "Months - Minutes", "Months - Hours", "Months - Days", "Months - Weeks", "Months - Years", "Years - Seconds", "Years - Minutes", "Years - Hours", "Years - Days", "Years - Weeks", "Years - Months"]
    print("Select Time Conversion".upper())
    for i, value in enumerate(units, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1 or response == 2 or response == 3 or response == 4 or response == 5 or response == 6:
                v1 = float(input("Enter Second Value: ".upper()))
                if response == 1:
                    ans1 = v1 * 0.0166667
                    print(f"{v1} second(s) is equal to {ans1} minute(s).")
                elif response == 2:
                    ans2 = v1 * 0.00027777833333
                    print(f"{v1} second(s) is equal to {ans2} hour(s).")
                elif response == 3:
                    ans3 = v1 / 86400
                    print(f"{v1} second(s) is equal to {ans3} day(s).")
                elif response == 4:
                    ans4 = v1 / 604800
                    print(f"{v1} second(s) is equal to {ans4} week(s).")
                elif response == 5:
                    ans5 = v1 / 2628000
                    print(f"{v1} second(s) is equal to {ans5} month(s).")
                elif response == 6:
                    ans6 = v1 / 31540000
                    print(f"{v1} second(s) is equal to {ans6} year(s).")
                break
            elif response == 7 or response == 8 or response == 9 or response == 10 or response == 11 or response == 12:
                v2 = float(input("Enter Minute Value: ".upper()))
                if response == 7:
                    ans7 = v2 * 60
                    print(f"{v2} minute(s) is equal to {ans7} second(s).")
                elif response == 8:
                    ans8 = v2 * 0.0166667
                    print(f"{v2} minute(s) is equal to {ans8} hour(s).")
                elif response == 9:
                    ans9 = v2 / 1440
                    print(f"{v2} minute(s) is equal to {ans9} day(s).")
                elif response == 10:
                    ans10 = v2 / 10080
                    print(f"{v2} minute(s) is equal to {ans10} week(s).")
                elif response == 11:
                    ans11 = v2 / 43800
                    print(f"{v2} minute(s) is equal to {ans11} month(s).")
                elif response == 12:
                    ans12 = v2 / 525600
                    print(f"{v2} minute(s) is equal to {ans12} year(s).")
                break
            elif response == 13 or response == 14 or response == 15 or response == 16 or response == 17 or response == 18:
                v3 = float(input("Enter Hour Value: ".upper()))
                if response == 13:
                    ans13 = v3 * 3600
                    print(f"{v3} hour(s) is equal to {ans13} second(s).")
                elif response == 14:
                    ans14 = v3 * 60
                    print(f"{v3} hour(s) is equal to {ans14} minute(s).")
                elif response == 15:
                    ans15 = v3 * 0.0416667
                    print(f"{v3} hour(s) is equal to {ans15} day(s).")
                elif response == 16:
                    ans16 = v3 / 168
                    print(f"{v3} hour(s) is equal to {ans16} week(s).")
                elif response == 17:
                    ans17 = v3 / 730
                    print(f"{v3} hour(s) is equal to {ans17} month(s).")
                elif response == 18:
                    ans18 = v3 / 8760
                    print(f"{v3} hour(s) is equal to {ans18} year(s).")
                break
            elif response == 19 or response == 20 or response == 21 or response == 22 or response == 23 or response == 24:
                v4 = float(input("Enter Day Value: ".upper()))
                if response == 19:
                    ans19 = v4 * 86400
                    print(f"{v4} day(s) is equal to {ans19} second(s).")
                elif response == 20:
                    ans20 = v4 * 1440
                    print(f"{v4} day(s) is equal to {ans20} minute(s).")
                elif response == 21:
                    ans21 = v4 * 24
                    print(f"{v4} day(s) is equal to {ans21} hour(s).")
                elif response == 22:
                    ans22 = v4 / 7
                    print(f"{v4} day(s) is equal to {ans22} week(s).")
                elif response == 23:
                    ans23 = v4 / 30.417
                    print(f"{v4} day(s) is equal to {ans23} month(s).")
                elif response == 24:
                    ans24 = v4 / 365
                    print(f"{v4} day(s) is equal to {ans24} year(s).")
                break
            elif response == 25 or response == 26 or response == 27 or response == 28 or response == 29 or response == 30:
                v5 = float(input("Enter Week Value: ".upper()))
                if response == 25:
                    ans25 = v5 * 604800
                    print(f"{v5} week(s) is equal to {ans25} second(s).")
                elif response == 26:
                    ans26 = v5 * 10080
                    print(f"{v5} week(s) is equal to {ans26} minute(s).")
                elif response == 27:
                    ans27 = v5 * 168
                    print(f"{v5} week(s) is equal to {ans27} hour(s).")
                elif response == 28:
                    ans28 = v5 * 7
                    print(f"{v5} week(s) is equal to {ans28} day(s).")
                elif response == 29:
                    ans29 = v5 / 4.345
                    print(f"{v5} week(s) is equal to {ans29} month(s).")
                elif response == 30:
                    ans30 = v5 / 52.143
                    print(f"{v5} week(s) is equal to {ans30} year(s).")
                break
            elif response == 31 or response == 32 or response == 33 or response == 34 or response == 35 or response == 36:
                v6 = float(input("Enter Month Value: ".upper()))
                if response == 31:
                    ans31 = v6 * 2628000
                    print(f"{v6} month(s) is equal to {ans31} second(s).")
                elif response == 32:
                    ans32 = v6 * 43800
                    print(f"{v6} month(s) is equal to {ans32} minute(s).")
                elif response == 33:
                    ans33 = v6 * 730.001
                    print(f"{v6} month(s) is equal to {ans33} hour(s).")
                elif response == 34:
                    ans34 = v6 * 30.4167
                    print(f"{v6} month(s) is equal to {ans34} day(s).")
                elif response == 35:
                    ans35 = v6 * 4.345
                    print(f"{v6} month(s) is equal to {ans35} week(s).")
                elif response == 36:
                    ans36 = v6 / 12
                    print(f"{v6} month(s) is equal to {ans36} year(s).")
                break
            elif response == 37 or response == 38 or response == 39 or response == 40 or response == 41 or response == 42:
                v7 = float(input("Enter Year Value: ".upper()))
                if response == 37:
                    ans37 = v7 * 31540000
                    print(f"{v7} year(s) is equal to {ans37} second(s).")
                elif response == 38:
                    ans38 = v7 * 525600
                    print(f"{v7} year(s) is equal to {ans38} minute(s).")
                elif response == 39:
                    ans39 = v7 * 8760
                    print(f"{v7} year(s) is equal to {ans39} hour(s).")
                elif response == 40:
                    ans40 = v7 * 365
                    print(f"{v7} year(s) is equal to {ans40} day(s).")
                elif response == 41:
                    ans41 = v7 * 52.1429
                    print(f"{v7} year(s) is equal to {ans41} week(s).")
                elif response == 42:
                    ans42 = v7 * 12
                    print(f"{v7} year(s) is equal to {ans42} month(s).")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")
    
def weight_conversion():
    units = ["Kilogram - Gram", "Kilogram - Milligram", "Kilogram - Pounds", "Kilogram - Ounce", "Kilogram - Tonne", "Gram - Kilogram", "Gram - Milligram", "Gram - Pounds", "Gram - Ounce", "Gram - Tonne", "Milligram - Kilogram", "Milligram - Gram", "Milligram - Pounds", "Milligram - Ounce", "Milligram - Tonne", "Pounds - Kilogram", "Pounds - Gram", "Pounds - Milligram", "Pounds - Ounce", "Pounds - Tonne", "Ounce - Kilogram", "Ounce - Gram", "Ounce - Milligram", "Ounce - Pounds", "Ounce - Tonne", "Tonne - Kilogram", "Tonne - Gram", "Tonne - Milligram", "Tonne - Pounds", "Tonne - Ounce"]
    print("Select Weight Conversion".upper())
    for i, value in enumerate(units, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1 or response == 2 or response == 3 or response == 4 or response == 5:
                v1 = float(input("Enter Kilogram Value: ".upper()))
                if response == 1:
                    ans1 = v1 * 1000
                    print(f"{v1} kg is equal to {ans1} g.")
                elif response == 2:
                    ans2 = v1 * 1000000
                    print(f"{v1} kg is equal to {ans2} mg.")
                elif response == 3:
                    ans3 = v1 * 2.20462
                    print(f"{v1} kg is equal to {ans3} lb(s).")
                elif response == 4:
                    ans4 = v1 * 35.274
                    print(f"{v1} kg is equal to {ans4} oz.")
                elif response == 5:
                    ans5 = v1 * 0.001
                    print(f"{v1} kg is equal to {ans5} t.")
                break
            elif response == 6 or response == 7 or response == 8 or response == 9 or response == 10:
                v2 = float(input("Enter Gram Value: ".upper()))
                if response == 6:
                    ans6 = v2 * 0.001
                    print(f"{v2} g is equal to {ans6} kg.")
                elif response == 7:
                    ans7 = v2 * 1000
                    print(f"{v2} g is equal to {ans7} mg.")
                elif response == 8:
                    ans8 = v2 * 0.00220462
                    print(f"{v2} g is equal to {ans8} lb(s).")
                elif response == 9:
                    ans9 = v2 * 0.035274
                    print(f"{v2} g is equal to {ans9} oz.")
                elif response == 10:
                    ans10 = v2 / 1000000
                    print(f"{v2} g is equal to {ans10} t.")
                break
            elif response == 11 or response ==  12 or response == 13 or response == 14 or response == 15:
                v3 = float(input("Enter Milligram Value: ".upper()))
                if response == 11:
                    ans11 = v3 / 1000000
                    print(f"{v3} mg is equal to {ans11} kg.")
                elif response == 12:
                    ans12 = v3 * 0.001
                    print(f"{v3} mg is equal to {ans12} g.")
                elif response == 13:
                    ans13 = v3 / 453592
                    print(f"{v3} mg is equal to {ans13} lb(s).")
                elif response == 14:
                    ans14 = v3 / 28350
                    print(f"{v3} mg is equal to {ans14} oz.")
                elif response == 15:
                    ans15 = v3 / 1000000000
                    print(f"{v3} mg is equal to {ans15} t.")
                break
            elif response == 16 or response == 17 or response == 18 or response == 19 or response == 20:
                v4 = float(input("Enter Pounds Value: ".upper()))
                if response == 16:
                    ans16 = v4 * 0.453592
                    print(f"{v4} lb(s) is equal to {ans16} kg.")
                elif response == 17:
                    ans17 = v4 * 453.592
                    print(f"{v4} lb(s) is equal to {ans17} g.")
                elif response == 18:
                    ans18 = v4 * 453592
                    print(f"{v4} lb(s) is equal to {ans18} mg.")
                elif response == 19:
                    ans19 = v4 * 16
                    print(f"{v4} lb(s) is equal to {ans19} oz.")
                elif response == 20:
                    ans20 = v4 * 0.000453592
                    print(f"{v4} lb(s) is equal to {ans20} t.")
                break
            elif response == 21 or response == 22 or response == 23 or response == 24 or response == 25:
                v5 = float(input("Enter Ounce Value: ".upper()))
                if response == 21:
                    ans21 = v5 * 0.0283495
                    print(f"{v5} oz is equal to {ans21} kg.")
                elif response == 22:
                    ans22 = v5 * 28.3495
                    print(f"{v5} oz is equal to {ans22} g.")
                elif response == 23:
                    ans23 = v5 * 28349.5
                    print(f"{v5} oz is equal to {ans23} mg.")
                elif response == 24:
                    ans24 = v5 * 0.0625
                    print(f"{v5} oz is equal to {ans24} lb(s).")
                elif response == 25:
                    ans25 = v5 / 35274
                    print(f"{v5} oz is equal to {ans25} t.")
                break
            elif response == 26 or response == 27 or response == 28 or response == 29 or response == 30:
                v6 = float(input("Enter Tonne Value: ".upper()))
                if response == 26:
                    ans26 = v6 * 1000
                    print(f"{v6} t is equal to {ans26} kg.")
                elif response == 27:
                    ans27 = v6 * 1000000
                    print(f"{v6} t is equal to {ans27} g.")
                elif response == 28:
                    ans28 = v6 * 1000000000
                    print(f"{v6} t is equal to {ans28} mg.")
                elif response == 29:
                    ans29 = v6 * 2204.62
                    print(f"{v6} t is equal to {ans29} lb(s).")
                elif response == 30:
                    ans30 = v6 * 35274
                    print(f"{v6} t is equal to {ans30} oz.")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def categories():
    categories = ["Distance/Length/Height", "Time", "Weight", "Pressure", "Power", "Frequency", "Energy", "Temparature", "Capacity", "Speed", "Area"]
    categories.sort()
    print("What would you be converting today?")
    for i, value in enumerate(categories, start = 1):
        print(f"{i}. {value}")
    while True:
        try:
            response = int(input("Enter Corresponding Number: ".upper()))
            if response == 1:
                area_conversion()
            elif response == 2:
                capacity_conversion()
            elif response == 3:
                distance_length_height_conversion()
            elif response == 4:
                energy_conversion()
            elif response == 5:
                frequency_conversion()
            elif response == 6:
                power_conversion()
            elif response == 7:
                pressure_conversion()
            elif response == 8:
                speed_conversion()
            elif response == 9:
                temperature_conversion()
            elif response == 10:
                time_conversion()
            elif response == 11:
                weight_conversion()
            else:
                print("Please enter a valid number.")
            question = input("Do You Have Anything Else To Convert? ")
            if question == "Yes" or question == "yes":
                continue
            else:
                print("Goodbye.")
                break
        except ValueError:
            print("Please enter a number.")

categories()