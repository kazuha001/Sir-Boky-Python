
arraysForLogIn = []

print("")

print("Dentist Appointment System")

print("")

print("Create New Account")

print("1. Create New Account")

print("2. Log in Existing Account")

def apointment():

    print("")

    print("Create New Account")

    print("")

    fnameId = input("Enter your first Name: ")

    print("")

    lnameId = input("Enter your Last Name: ")
    
    print("")

    birthId = int(input("Enter your Age: "))

    print("")

    birthIdresult = int(2024 - birthId)
    
    arraysForLogIn.append(birthIdresult)

    print(fnameId, lnameId, birthIdresult)
    

choose = input("Choose: ")

if choose == '1':
    apointment()
else:
    print("exit")
