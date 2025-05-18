A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age = int(input("How old are you?"))
if age > 17:
    print("You can see G, PG-13, and R movies")
elif age >12:
    print("You can see G and PG-13 movies")
else:
    print("You can see G movies")
