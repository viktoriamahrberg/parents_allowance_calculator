print("\nWelcome to your Parent's Allowance Calculator. \nYou can use this calculator to find out about what your annual pay when on maternity-/paternity leave will be.")
print("The allowance is based on 80% of your gross salary and a 30% tax deduction on top of that.\n")

def get_income_data():
    """
    Collects the gross annual salary from user
    """
    print("Please enter your annual gross salary (5-7 digits only)\nExample: 450000\n")
    data_str = input("Enter your salary here:\n")
    print(data_str)

get_income_data()
