#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
#State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
#* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
#* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
#* Children (0-18): Free.
def ferry_fare(age, vehicle):
    if age <= 18:
        return "Child: Free"
    elif age > 19 and age < 65:
        if vehicle == "Yes":
            return "Adult: $20"
        else:
            return "Adult: $10"
    elif age >= 65:
        if vehicle == "Yes":
            return "Senior: $15"
        else:
            return "Senior: $5"
print(ferry_fare(18, "Yes"))
print(ferry_fare(12, "No"))
print(ferry_fare(45, "Yes"))
print(ferry_fare(21, "No"))
print(ferry_fare(70, "Yes"))
print(ferry_fare(67, "No"))
