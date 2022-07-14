import Task1 as T1
import Task2 as T2
import Task3 as T3
import Task4 as T4
import CarRental as C
import re


def readFile(company):
    try:
        fo = open("CarRentalOld.txt", "r")
        Line_exists = fo.readline()  # Read 1 line
        flag = 1  # to know if there is information in the file or no
        while Line_exists:
            Line_exists = re.sub(r'\n', "", Line_exists)  # remove \n
            fields = list(Line_exists.split(";"))
            flag = 0
            if len(fields) != 10:
                print("Wrong Details in the file!")
                company.__del__()
                break
            company.add(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7],
                        fields[8],
                        fields[9])
            Line_exists = fo.readline()
        if flag:
            print("No Information in this file!\n")
        fo.close()
    except IOError:
        print("Error: can't find file or read data")


def readOption():
    return input("Please Enter Number Of Option To Execute:\n"
                 "1. Inquiry About A Person.\n"
                 "2. Inquiry About A Car\n"
                 "3. Add A New Car Rental.\n"
                 "4. Show Statistics About Each Car.\n"
                 "5. Exit Program.\n")


def printMissingSummary(company):
    print("           Summary of data missing in the database:"
          "\nNumber of duplicate entries in the database = " + str(company.nDuplicates) +
          "\nNumber of entries with wrong date format in the database = " + str(company.nDatechange) +
          "\nNumber of entries where names are dropped from the database = " + str(company.nDropnames) +
          "\nNumber of entries where Ids are dropped from the database = " + str(company.nDropids) +
          "\nNumber of entries where dob are dropped from the database = " + str(company.nDropdob) +
          "\nNumber of entries where mobile numbers are dropped from the database = " + str(company.nDropmobiles) +
          "\nNumber of entries where personal entry can not be completed = " + str(company.nDroppentry) +
          "\nNumber of entries where car make is dropped from the database = " + str(company.nDropcmake) +
          "\nNumber of entries where car Ids are dropped from the database = " + str(company.nDropcids) +
          "\nNumber of entries where car models (year) are dropped from the database = " +
          str(company.nDropcyears) + "\n")


def printCompletedSummary(company):
    print("           Summary of data recovered from the database:"
          "\nNumber of duplicate entries removed from the new database = " + str(company.nDuplicates) +
          "\nNumber of entries with wrong date format fixed in the new database = " + str(company.nDatechange) +
          "\nNumber of entries with names recovered in the new database = " + str(company.nDropnames) +
          "\nNumber of entries with Ids recovered in the new database = " + str(company.nDropids) +
          "\nNumber of entries with dob recovered in the new database = " + str(company.nDropdob) +
          "\nNumber of entries with mobile numbers recovered in the new database = " + str(company.nDropmobiles) +
          "\nNumber of entries with car make recovered in the new database = " + str(company.nDropcmake) +
          "\nNumber of entries with car models (year) recovered in the new database = " +
          str(company.nDropcyears) + "\n")


####################################
############## MAIN ################
try:
    company118 = C.Company()
    readFile(company118)
    printMissingSummary(company118)
    printCompletedSummary(company118)
    T1.moveDataBase(company118)
    while 1:
        Option = readOption()
        if Option == '1':
            T2.inquiryPerson(company118)
        elif Option == '2':
            T2.inquiryCar(company118)
        elif Option == '3':
            T3.newCarRental(company118)
        elif Option == '4':
            T4.carStatistics(company118)
        elif Option == '5':
            break
        else:
            print("Wrong Input!\n")
except Exception:
    print("There Is At Least One Error!")
