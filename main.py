
arraysForFirst = []

arraysForLast = []

arraysForAge = []

arraysForBirth = []

arraysForMinors = []

arraysForDates = []

arraysForTime = []

arraysForDays = []

def appointment():

    loop1 = True

    while loop1:

        print("")

        print("Dentist Appointment System")
    
        print("")

        print("1. Add New Appointments")

        print("2. Remove Appointments")

        print("3. Update Appointments")

        print("4. Display Appointments")

        print("5. Display all")

        print("0. Exit the Program")

        print("")

        choose = input("Choose: ")

        if choose == '1':

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
            
            
            if birthId <= 18:
            
                doctorOrpatientId_result = "Minor"
                    
                arraysForMinors.append(doctorOrpatientId_result)
                
            else:
            
                doctorOrpatientId_result = "Adult"
                    
                arraysForMinors.append(doctorOrpatientId_result)

            dateId = input("Months: ")
            arraysForDates.append(dateId)

            print("")

            timeId = input("time: ")
            arraysForTime.append(timeId)

            print("")

            dayId = input("Days: ")
            arraysForDays.append(dayId)

            print("")

            print("Sucessfully Submited")

        elif choose == '2':

            print("Users Appointments: ", arraysForFirst)

            nameId = input("Remove: ")

            if nameId in arraysForFirst:

                userId = arraysForFirst.index(nameId)

                arraysForFirst.pop(userId)

                arraysForLast.pop(userId)

                arraysForAge.pop(userId)

                arraysForBirth.pop(userId)

                arraysForMinors.pop(userId)

                arraysForTime.pop(userId)

                arraysForDays.pop(userId)

                arraysForDates.pop(userId)

                print("Remove Sucesfully... ")

            else:

                print("Invalid")

        elif choose == '3':

            print("Update Appointments: ", arraysForFirst)

            nameId = input("Update: ")

            if nameId in arraysForFirst:

                userId = arraysForFirst.index(nameId)

                arraysForFirst.pop(userId)

                arraysForLast.pop(userId)

                arraysForAge.pop(userId)

                arraysForBirth.pop(userId)

                arraysForMinors.pop(userId)

                arraysForTime.pop(userId)

                arraysForDays.pop(userId)

                arraysForDates.pop(userId)

                fnameId = input("Enter your First Name: ")
                arraysForFirst.insert(userId, fnameId)

                print("")

                lnameId = input("Enter your Last Name: ")
                arraysForLast.insert(userId, lnameId)

                print("")

                birthId = int(input("Enter your Age: "))
                arraysForAge.insert(userId, birthId)

                print("")

                birthIdresult = int(2024 - birthId)
                arraysForBirth.insert(userId, birthIdresult)
                
                
                if birthId <= 18:
                
                    doctorOrpatientId_result = "Minor"
                        
                    arraysForMinors.insert(userId, doctorOrpatientId_result)
                    
                else:
                
                    doctorOrpatientId_result = "Adult"
                        
                    arraysForMinors.insert(userId,doctorOrpatientId_result)

                dateId = input("Months: ")
                arraysForDates.insert(userId, dateId)

                print("")

                timeId = input("time: ")
                arraysForTime.insert(userId, timeId)

                print("")

                dayId = input("Days: ")
                arraysForDays.insert(userId, dayId)

                print("")

                print("Sucessfully Updated")

            else:
                
                print("Invalid")
        elif choose == '4':

            print("Display Appointments: ", arraysForFirst)

            nameId = input("Display: ")

            if nameId in arraysForFirst:

                userId = arraysForFirst.index(nameId)

                fnameId = arraysForFirst[userId]

                lnameId = arraysForLast[userId]

                birthId = arraysForAge[userId]

                birthIdresult = arraysForBirth[userId]

                dateId = arraysForDates[userId]

                timeId = arraysForTime[userId]

                dayId = arraysForDays[userId]

                print("")

                print("Name:", fnameId, lnameId)

                print("Birth Year:", birthIdresult, "Age:", birthId)

                print("Appointments Scheduled")

                print("Months:", dateId, dayId, "2024","Time:", timeId)

                print("")


        else:

            break
        

appointment()