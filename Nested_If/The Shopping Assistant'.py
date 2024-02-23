#Tasks:1,2,3


clothing = ["sunglasses", "umbrella", "sweater"]

weather = input("Enter the weather: sunny, rainy, or cold: ")
if weather == "sunny" and not "rainy":
    print("Go for a walk in the park, with your sunglasses on!")
elif weather == "rainy" or not "cold":
    print("Use an umbrella")
elif weather == "rainy":
    print("Were some boots")
elif weather == "cold":
    print("wear a sweater!")
else:
    print("Stay home!")

