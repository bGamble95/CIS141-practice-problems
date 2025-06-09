#2. Write a Python program that allows users to log their hiking trips. The program
#should:
#- Use a while loop to repeatedly ask for a hike name and distance in miles
#- Save each entry to hiking_log.txt (each hike on a new line)
#- When the user presses 0, exit the loop & print the contents of hiking_log.txt

file = open("hiking_log.txt", "a")
while True:
    hike_name = input("Enter hike name or press 0 to exit ")
    if hike_name == "0":
        break
    distance = input("How many miles was the hike? ")
    file.write(hike_name + "\t" + distance + "\n")
file.close()
