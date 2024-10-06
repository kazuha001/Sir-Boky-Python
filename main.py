
arraysForFirst = []

arraysForLast = []

arraysForAge = []

arraysForBirth = []

arraysForUser = []

arraysForPass = []

print("")

print("Dentist Appointment System")
loop1 = True

while loop1:

    print("")

    print("Create New Account")

    print("1. Create New Account")

    print("2. Log in Existing Account")

    def createAccount():

        print("")

        print("Personal Information")

        print("")

        fnameId = input("Enter your First Name: ")
        arraysForFirst.append(fnameId)

        print("")

        lnameId = input("Enter your Last Name: ")
        arraysForLast.append(lnameId)

        print("")

        birthId = int(input("Enter your Age: "))
        arraysForAge.append(birthId)

        print("")

        birthIdresult = int(2024 - birthId)
        arraysForBirth.append(birthIdresult)
    
        print("")

        print("Create New User...")

        print("")

        userId = input("Enter your Username: ")
        arraysForUser.append(userId)


        print("")

        loop0 = True
    
        while loop0:

            passId = input("Enter your Password: ")

            passId_confirm = input("Confirm your Password: ")

            if passId_confirm != passId:

                loop0 = True

                print("Incorrect Confirmation Password")

            else:

                print("Submitted Successfully")
                arraysForPass.append(passId_confirm)
            
                break

    


    def logInAccount():

        loop2 = True

        while loop2:
            
            print("Username: ")
            inputUserId = input()
            print("Password: ")
            inputPassId = input()

            indexUserId = arraysForUser.index(inputUserId)

            indexPassId = arraysForPass.index(inputPassId)

            if inputUserId in arraysForUser and inputPassId in arraysForPass:

                if indexUserId != indexPassId:

                    print("Invalid Password... ")

                    loop2 = True
                
                else:

                    print("Sucessfully Log In... ")

                    break
            
            else:

                print("No Existing Account")

    
    loop1 = True

    choose = input("Choose: ")

    if choose == '1':

        createAccount()


    elif choose == '2':

        logInAccount()

    else:
        print("exit")

        break

