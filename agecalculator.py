from datetime import datetime

def calculate_age(birthdate):
    try:

        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        

        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        return age
    except ValueError as e:
        raise ValueError("Invalid date format. Please enter the date in the format YYYY-MM-DD. Error: {}".format(e))

def main():

    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

    try:

        age = calculate_age(birthdate_input)
        print("Your age is:", age)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
