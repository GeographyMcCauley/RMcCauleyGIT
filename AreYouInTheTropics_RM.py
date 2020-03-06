lat = int(input("Enter your line of Latitude: "))
if lat > 90 or lat < -90:
    print("Out of Bounds: ")
elif lat == 0:
    print("At the Equator: ")
elif lat > 0 and lat <=23.5:
    print("In Northern Hemisphere: ")
    print("You are in the Tropics: ")
elif lat > 23.5:
    print("You are in the Northern Hemisphere: ")
    print("You are not in the Tropics: ")
elif lat < 0 and lat >= -23.5:
    print("In Southern Hemisphere: ")
    print("You are in the Tropics: ")
elif lat <-23.5:
    print("In Southern Hemisphere: ")
    print("You are not in the tropics: ")