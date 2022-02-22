""" Sleep function imported to delay print statement
in the end of program
"""
from time import sleep

# Print color text feature from StockOverflow
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
WARNING = '\033[93m'
ENDC = '\033[0m'
OKCYAN = '\033[96m'
OKBLUE = '\033[94m'


def get_income_data():
    """
    Collects the gross annual salary from user
    """
    while True:
        try:
            print("Please enter your annual gross salary")
            print("Example: 450000\n")
            data_str = input("Enter your salary here:\n")
            annual_wage = int(data_str)
            break
        except ValueError:
            print(WARNING+"You entered the salary incorrectly.")
            print("Please enter a valid number\n"+ENDC)
    return annual_wage


def calculate_annual_allowance(annual_wage):
    """
    Calculates yearly allowance based on yearly salary;
    80% of gross salary minus taxes of 70%
    """
    annual_allowance = (annual_wage * 0.8 * 0.7)
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
        try:
            monthly_days = int(input("Enter your amount of days here:\n"))
        except ValueError:
            print(WARNING+"You entered invalid data,")
            print("please try again."+ENDC)
            continue
        if monthly_days < 31:
            print(f"You wish you take {monthly_days} days.\n")
            break
        elif monthly_days > 31:
            print(WARNING+"The number you entered is invalid."+ENDC)
            continue

    return monthly_days


def enter_month():
    """
    Checks whether the entered month is a valid month
    """
    months_available = (
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
        )
    while True:
        chosen_month_str = input("Enter the month to base calculations on:\n")
        input_month = str.lower(chosen_month_str)

        if input_month in months_available:
            break

        else:
            print(WARNING+"The month you entered")
            print("is invalid, please try again."+ENDC)
    return input_month


def calculate_monthly_allowance(monthly_days, annual_allowance, input_month):
    """
    Takes the yearly allowance and divide with 365 days
    to get the allowance per day and multiply with the users requested
    days
    """

    daily_allowance = annual_allowance / 365
    monthly_result = daily_allowance * monthly_days

    print(OKCYAN+"Based on the numbers you have provided you will recieve")
    print(f"{round(monthly_result)} SEK/month in the")
    print(f"month of {input_month.capitalize()}"+ENDC)


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
    annual_wage = get_income_data()
    annual_allowance = calculate_annual_allowance(annual_wage)
    monthly_days = get_monthly_days()
    input_month = enter_month()
    calculate_monthly_allowance(monthly_days, annual_allowance, input_month)
    sleep(2)
    print("Thanks for using the Parental Allowance Calculator")


main()
