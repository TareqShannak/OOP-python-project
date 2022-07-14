import datetime
import re


def modifiedDate(date):
    if date != '': # 5/4/2020
        dateFields = list(re.split('[-/]', date))
        if len(dateFields) == 1:
            return date
        x = datetime.datetime(int(dateFields[2]), int(dateFields[1]), int(dateFields[0]))
        date = x.strftime("%d %B %Y")
    return date


def fixCarInfo(rent, newRent):
    if rent.getCM() == '':
        rent.setCM(newRent["CM"])
    elif newRent["CM"] == '':
        newRent["CM"] = rent.getCM()
    if rent.getYear() == '':
        rent.setYear(newRent["Year"])
    elif newRent["Year"] == '':
        newRent["Year"] = rent.getYear()


def fixPersonInfo(rent, newRent):
    if rent.getName() == '':
        rent.setName(newRent["Name"])
    elif newRent["Name"] == '':
        newRent["Name"] = rent.getName()
    if rent.getDoB() == '':
        rent.setDoB(newRent["DoB"])
    elif newRent["DoB"] == '':
        newRent["DoB"] = rent.getDoB()
    if rent.getMobile == '':
        rent.setMobile(newRent["Mobile"])
    elif newRent["Mobile"] == '':
        newRent["Mobile"] = rent.getMobile()


def writeOnFile(fo, obj, rent):
    try:
        fo.write(
            obj.getName() + ";" + obj.getId() + ";" + obj.getDoB() + ";" + obj.getMobile() + ";" + rent.getCL() + ";" +
            rent.getCM() + ";" + rent.getYear() + ";" + rent.getSD() + ";" + rent.getED() + ";" + rent.getRB() + "\n")
    except IOError:
        print("Error: can't write data on the file")


def moveDataBase(company):
    try:
        foCompleted = open("CarRentalCompleted.txt", "w")
        foMissing = open("CarRentalMissing.txt", "w")
        for obj in company.getListOfPeople():
            if obj.getName() == '' or obj.getId() == '' or obj.getDoB() == '' or obj.getMobile() == '':
                for rent in obj.getlistOfRents():
                    writeOnFile(foMissing, obj, rent)
            else:
                for rent in obj.getlistOfRents():
                    if (
                            rent.getCL() == '' or rent.getCM() == '' or rent.getYear() == '' or rent.getSD() == '' or
                            rent.getED() == '' or rent.getRB() == ''):
                        writeOnFile(foMissing, obj, rent)
                    else:
                        writeOnFile(foCompleted, obj, rent)
        foMissing.close()
        foCompleted.close()
    except IOError:
        print("Error: can't write data or find file")


def isDuplicatedPerson(person, CL, CM, Year, SD, ED, RB):
    for rent in person.getlistOfRents():
        if (rent.getCL() == CL and rent.getCM() == CM and rent.getYear() == Year and rent.getSD() == SD and
                rent.getED() == ED and rent.getRB() == RB):
            return 1
    return 0


def isDuplicatedCar(car, Name, Id, DoB, Mobile, SD, ED, RB):
    for rent in car.getlistOfRents():
        if (
                rent.getName() == Name and rent.getId() == Id and rent.getDoB() == DoB and rent.getMobile() ==
                Mobile and rent.getSD() == SD and rent.getED() == ED and rent.getRB() == RB):
            return 1
    return 0
