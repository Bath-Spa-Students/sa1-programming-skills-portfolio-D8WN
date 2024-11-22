# Loops | Pizza Toppings:

Topping_Count = 0
Max_Toppings = 5

while Topping_Count < Max_Toppings:
    Topping = input(f"Enter Topping {Topping_Count + 1} of {Max_Toppings}: ")
    print(f"Good Choice!, we will add {Topping} on your pizza.")
    Topping_Count += 1

print("Maximum number of pizza toppings has been added.")