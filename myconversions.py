# Modules

print("My Module is running!")

def fromcelcius():
    usertemp = input(("Enter the temperature that you want to covert to degrees F: "))
    temp = float(usertemp)
    print(type(temp))
    return((temp *1.8) + 32)
def fromfahrenheit(value):
    return(value-32) / 1.8
    