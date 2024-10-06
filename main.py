
arraysForFirst = []

arraysForLast = []

arraysForAge = []

arraysForBirth = []

arraysForUser = []

arraysForPass = []

arraysForAppointment = []

arraysForDoctorOrPatient = []

loop1 = True

while loop1:
    
    print("")

    print("Dentist Appointment System")
    
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
        
        loop3 = True
        
        while loop3:
        
            print("You are a Doctor or Patient? ")
        
            print("")
        
            print("1. Doctor")
        
            print("2. Patient")
        
            doctorOrpatientId = input("Choose: ")
        
            if doctorOrpatientId == '1':
        
                doctorOrpatientId_result = "Doctor"
                
                arraysForDoctorOrPatient.append(doctorOrpatientId_result)
             
                break
            
            elif doctorOrpatientId == '2':
        
                doctorOrpatientId_result = "Patient"
                
                arraysForDoctorOrPatient.append(doctorOrpatientId_result)
                
                break
            
            else:
        
                loop3 = True
        
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
            
            print("")

            print("Log In...")

            print("")

            inputUserId = input("Username: ")
            inputPassId = input("Password: ")
            
            if inputUserId in arraysForUser and inputPassId in arraysForPass:
            
                indexUserId = arraysForUser.index(inputUserId)

                indexPassId = arraysForPass.index(inputPassId)

                if indexUserId != indexPassId:

                    print("Invalid Password... ")

                    loop2 = True
                
                else:
                    
                    print("")

                    print("Sucessfully Log In... ")
                    
                    print("")

                    print("Welcome ", inputUserId)

                    if indexUserId == indexPassId:

                        print("Account Information")

                        print("Account Id No. ", indexUserId)
                        
                        fnamePopArrays = arraysForFirst.pop(indexUserId)
                        
                        print("Hellow, ", fnamePopArrays)

                        print("")

                        print("Choose... ")

                        print("")

                        print("1. Create New Appointment")

                        print("2. View  Appointment")

                        print("3. Delete Appointment")

                        print("4. Update Appointment")

                        chooseAppointment = input("Choose: ")
                        
                        break
                        
                        fnamePopArrays = arraysForFirst.pop()
                        
                    else:

                        break
                    
            else:
                
                print("")

                print("Invalid")

                break
    
    loop1 = True

    choose = input("Choose: ")

    if choose == '1':

        createAccount()


    elif choose == '2':

        logInAccount()

    else:
        print("exit")

        break

