# Exercise 05: Days of the Month

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
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

try:
    month = int(input("Enter the month number (1-12): "))
    year = int(input("Enter the year: "))

    if 1 <= month <= 12:
        if month == 2:
            if is_leap_year(year):
                print(f"February in {year} has 29 days.")
            else:
                print(f"February in {year} has 28 days.")
        else:
            print(f"The month {month_names[month]} has {month_days[month]} days.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")