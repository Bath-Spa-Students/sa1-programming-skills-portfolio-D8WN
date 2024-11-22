# Exercise 06: Brute Force Attack
# Optional Requirement

Password = "12345"

while Password:
    User_Attempts = input("Please enter the password: ")
    
    if User_Attempts == Password:
        print("You have succesfully entered the password. Access granted, Welcome back Mr. Bruce Wayne.")
        break  
    else:
        print("Incorrect password. Please try again.")