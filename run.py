import math


# Class from StockOverflow

WARNING = '\033[93m'
ENDC = '\033[0m'


def get_income_data():
    """
    Collects the gross annual salary from user
    """
    while True:
        print("Please enter your annual gross salary (5-7 digits only)")
        print("Example: 450000\n")
        data_str = input("Enter your salary here:\n")

        if (data_str := validate_annual_data(data_str)):
            break
    return data_str


def validate_annual_data(values):
    """
    Checks if data (salary) has been inserted as values and throws an error message if it's wrongly input.
    """
    try:
        annual_salary = int(values)
        print(f"You entered {annual_salary}")

    except ValueError:
        print(WARNING+"You entered the salary incorrectly.")
        print("Please enter a valid number\n" + ENDC)
        return False

    return annual_salary


def calculate_annual_allowance(values):
    """
    Calculates yearly allowance based on yearly salary; 
    80% of gross salary minus taxes of 70%
    """


def main():
    print("\nWelcome to your Parent's Allowance Calculator. \nYou can use this calculator to find out about what your annual pay when on maternity-/paternity leave will be.")
    print("The allowance is based on 80% of your gross salary and a 30% tax deduction on top of that.\n")
    wage = get_income_data()
    print(type(wage))
    # validated_wage = validate_annual_data(wage)

    # calc_amount = calculate_annual_allowance(validated_wage)
    # print(type(validated_wage))


main()