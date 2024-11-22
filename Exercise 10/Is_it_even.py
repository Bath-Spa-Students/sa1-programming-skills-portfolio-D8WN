# Exercise 10: Is it even?

print("Is it an ODD or EVEN number?")
def even(number): 
    return number % 2 == 0  
def odd(number): 
    return number % 2 == 1 
def main():
    number= int(input("Place a number here: ")) 

    if even(number): 
        print("That number is considered an EVEN number.")
    elif odd(number): 
        print("That number is considered an ODD number.")
main()