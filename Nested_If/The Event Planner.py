#Tasks1:

attendees = input("Enter number of attendees: ")

if attendees > 100:
    print("large hall")
else:
    print("conference room")


#Tasks2:
attendees = input("Enter number of attendees: ")

if attendees > 100:
    print("large hall")
elif attendees <= 100 and attendees > 0:
    print("medium hallsize")
else:
    print("conference room")




#Tasks3:

attendees = input("Enter number of attendees: ")

if attendees > 100:
    print("large hall")
elif attendees > 100 and attendees <= 500:
    print("Huge hall room, with some catering")
else:
    print("conference room")
