# Temperature (°C),Print
# Below 10,"Cold, wear a jacket"
# 10 to 25,Pleasant
# 26 to 35,Warm
# Above 35,"Very hot, stay hydrated"

temp =float(input("Enter temprature in celcius : "))
if temp<10:
    print("Cold ,wear a jacket")
elif temp<=25:
    print("Pleasant")
elif temp<=35:
    print("Warm")
else:
    print("Very hot, stay hyderated")
