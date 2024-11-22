# Exercise 06: Brute Force Attack

# Define the correct password
correct_password = "secret123"

# While loop to keep asking for the password until the correct one is entered
while True:
    # Ask the user to input the password
    user_input = input("Please enter the password: ")
    
    # Check if the entered password is correct
    if user_input == correct_password:
        print("Password accepted. Access granted.")
        break  # Exit the loop if the correct password is entered
    else:
        print("Incorrect password. Please try again.")