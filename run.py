# Class from StockOverflow 
class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'

print("\nWelcome to your Parent's Allowance Calculator. \nYou can use this calculator to find out about what your annual pay when on maternity-/paternity leave will be.")
print("The allowance is based on 80% of your gross salary and a 30% tax deduction on top of that.\n")

def get_income_data():
    """
    Collects the gross annual salary from user
    """
    while True:
        print("Please enter your annual gross salary (5-7 digits only)\nExample: 450000\n")
        data_str = input("Enter your salary here:\n")
        
        if validate_annual_data(data_str):
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
        print(bcolors.WARNING + "You entered the salary incorrectly. Please enter a valid number\n" + bcolors.ENDC)
        return False
        
    return True

def calculate_annual_allowance(value):
   print("hola")

data_str = get_income_data()
calculate_annual_allowance(data_str)
#calculate_annual_allowance()
