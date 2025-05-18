A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.
 order = int(input("How much was your order?"))
if order >= 50:
    order_total = order
else:
    order_total = order + 5
print(order_total)                                                                                                                                                                      
