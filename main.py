
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
            
            
            if birthId <= 18:
            
                doctorOrpatientId_result = "Minor"
                    
                arraysForMinors.append(doctorOrpatientId_result)
                
            else:
            
                doctorOrpatientId_result = "Adult"
                    
                arraysForMinors.append(doctorOrpatientId_result)

            print("")
            print("Appointments Details")
            print("")
            print("Choose Months")
            print("")
            print("1. January")
            print("2. Febuary")
            print("3. March")
            print("4. April")
            print("5. May")
            print("6. June")
            print("7. July")
            print("8. August")
            print("9. September")
            print("10. October")
            print("11. November")
            print("12. December")
            print("")
            dateId = input("Months: ")
            
            if dateId == '1':

                dateId_result = "January"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    return

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)


            elif dateId == '2':
                
                dateId_result = "Febuary"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()
                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '3':
                
                dateId_result = "March"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '4':
                
                dateId_result = "April"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '5':
                
                dateId_result = "May"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '6':
                dateId_result = "June"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()
                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '7':
                dateId_result = "July"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '8':
                dateId_result = "August"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '9':
                dateId_result = "September"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '10':
                dateId_result = "October"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '11':
                dateId_result = "November"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)
            elif dateId == '12':
                dateId_result = "December"

                print("")
                print("Choose Days... ")
                print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
                print("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
                print("21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                print("31")

                daysId = int(input("Choose: "))

                if daysId >= 31 and daysId <= 0:

                    print("Invalid")
                    exit()

                else:
                    arraysForDates.append(dateId_result)
                    arraysForDays.append(daysId)

            print("")

            

            timeId = input("time: ")
            
            print("")
            print("A.M. or P.M? ")
            print("")

            print("1. A.M.")
            print("2. P.M.")

            timeId2 = input("Choose: ")
            if timeId2 == '1':
                timeId = timeId, "a.m."
                arraysForTime.append(timeId)
            elif timeId2 == '2':
                timeId = timeId, "p.m."
                arraysForTime.append(timeId)
            else:
                return
            

            print("")

            print("Sucessfully Submited")

            print("")

            input("Click Enter")

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
            
            print("")

            input("Click Enter")

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

            print("")
            input("Click Enter")
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
            print("")
            input("Click Enter")

        elif choose == '5':

            print("All Appointments")

            for value, value1, value2, value3, value4, value5, value6, value7 in zip(arraysForFirst, arraysForLast, arraysForBirth, arraysForAge, arraysForMinors, arraysForDates, arraysForDays, arraysForTime):
                
                if len(arraysForFirst) > 0:
                    print("")
                    print("-------------------------------------------------")
                    print("Personal Information")
                    print("")
                    print("First Name:", value, "Last Name:", value1)
                    print("Birth-Year:", value2, "Age:", value3)
                    print("You Are:", value4)
                    print("")
                    print("-------------------------------------------------")
                    print("Appointments Details")
                    print("")
                    print("Months:", value5, value6, "Time:", value7)
                    print("-------------------------------------------------")
                    print("")
                else:
                    print("No Appoinments... ")
            print("")
            input("Click Enter")
        else:

            break
        

appointment()