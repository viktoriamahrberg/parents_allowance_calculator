"""
Color error message feature from StockOverflow
"""
WARNING = '\033[93m'
ENDC = '\033[0m'
OKCYAN = '\033[96m'


def get_income_data():
    """
    Collects the gross annual salary from user
    """
    while True:
        print("Please enter your annual gross salary")
        print("Example: 450000\n")
        data_str = input("Enter your salary here:\n")

        if (data_str := validate_annual_data(data_str)):
            break
    return data_str


def validate_annual_data(values):
    """
    Checks if data (salary) has been inserted as values
    and throws an error message if it's wrongly input.
    """
    try:
        annual_salary = int(values)
        print(f"You entered {annual_salary}")

    except ValueError:
        print(WARNING+"You entered the salary incorrectly.")
        print("Please enter a valid number\n"+ENDC)
        return False

    return annual_salary


def calculate_annual_allowance(wage):
    """
    Calculates yearly allowance based on yearly salary;
    80% of gross salary minus taxes of 70%
    """

    annual_allowance = (wage * 0.8 * 0.7)
    print(OKCYAN+"Your total annual allowance would be:")
    print(f"{round(annual_allowance)} SEK"+ENDC)
    # Enter function from StockOverflow
    # https://stackoverflow.com/questions/42077811/how-do-i-have-a-press-enter-to-continue-feature-in-python
    input('Press Enter to continue..')
    return annual_allowance


def get_monthly_days():
    """
    Collects the total days per month the user wishes to be on leave
    """
    while True:
        print("\nPlease enter the amount of days per month you wish")
        print("to be on leave for and thereby also get allowance for\n")
        monthly_days = input("Enter your amount of days here:\n")
        int_days = validate_days_data(monthly_days)

        if validate_days_data(int_days):
            print(f"You wish to take {int_days} days of leave")
            break

    return int_days
     

def validate_days_data(monthly_days):
    """
    Checks if entered days are equal or less to a months 31 days
    """
    int_days = int(monthly_days)
    try:
        if int_days > 31:
            raise ValueError(
                f"You entered {int_days} days,"
                )
    except ValueError as e:
        print(WARNING+f"The number you entered is invalid:{e}")
        print("please try again."+ENDC)
        return False

    return int_days


def enter_month():
    """
    Checks whether the entered month is a valid month
    """
    months_available = ("january", "february", "march", "april", "may",
    "june", "july", "august", "september", "october", "november", "december")
    while True: 
        chosen_month = str(input("Enter the month to base calculations on\n"))     
        
        entered_month = False 

        if chosen_month in months_available:
            entered_month = True
            break

        else:
            raise TypeError(
                f"You entered {chosen_month},"
                )
            print(WARNING+"The data you entered is invalid.")
            print("Please try again."+ENDC)


    return chosen_month      


def calculate_monthly_allowance(int_days, annual_allowance, chosen_month):
    """
    Takes the yearly allowance and divide with 365 days
    to get the allowance per day and multiply with the users requested
    days
    """

    daily_allowance = annual_allowance / 365
    monthly_result = daily_allowance * int_days

    print(OKCYAN+"Based on the numbers you have provided you will recieve")
    print(f"{round(monthly_result)} SEK/month in the month of {chosen_month}"+ENDC)


def main():
    """
    Run the program functions
    """
    print("\nWelcome to your Parent's Allowance Calculator.\n")
    print("You can use this calculator to find out about what your")
    print("annual pay when on maternity-/paternity leave will be.")
    print("The allowance is based on 80% of your gross salary and a")
    print("30% tax deduction on top of that.\n")
    print("Please note the calculations are done in Swedish Kronor (SEK)")
    wage = get_income_data()
    annual_allowance = calculate_annual_allowance(wage)
    int_days = get_monthly_days()
    chosen_month = enter_month()
    calculate_monthly_allowance(int_days, annual_allowance, chosen_month)


main()
