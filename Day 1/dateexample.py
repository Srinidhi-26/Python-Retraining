from datetime import datetime, timedelta

def check_age(birthdate, joiningdate):
    date_format = "%d.%m.%Y"
    dt1 = datetime.strptime(birthdate, date_format)
    dt2 = datetime.strptime(joiningdate, date_format)
    diff_years = (dt2 - dt1) // timedelta(days=365.2425)

    if diff_years >= 18:
        return True
    else:
        return False

def call():
    birthdate = input("Enter birth date in dd.mm.yyyy format: ")
    joiningdate = input("Enter joining date in dd.mm.yyyy format: ")
    if check_age(birthdate, joiningdate):
        print("The birth date is 18 years earlier")
    else:
        print("The birth date is not at least 18 years earlier")

call();
