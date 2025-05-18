The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
threshold = int(input("What is the current daylight threshold?"))
if threshold < 8:
    print("Headlights On")
else:
    print("Headlights Off")
