import math
side1 = int(input("Enter first side of triangle"))
side2 = int(input("Enter second side of triangle"))
side3 = int(input("Enter third side of triangle"))
semi_pemi = (side1+side2+side3)/2
heron = math.sqrt(semi_pemi*(semi_pemi-side1)*(semi_pemi-side2)*(semi_pemi-side3))
print(heron)

