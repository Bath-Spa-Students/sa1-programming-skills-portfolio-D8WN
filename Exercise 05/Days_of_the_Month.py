month_days = {
    1: 31, 
    2: 28,  
    3: 31,   
    4: 30,   
    5: 31,  
    6: 30,   
    7: 31,  
    8: 31,  
    9: 30,   
    10: 31, 
    11: 30, 
    12: 31   
}

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"}

month_number = int(input("Enter the month number (1-12): "))

if 1 <= month_number <= 12:
    print(f"The number of days in month {month_names[month_number]} is {month_days[month_number]}")

else:
    print("Invalid month number. Please enter a number between 1 and 12.")