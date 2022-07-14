import Task1 as T1

def checkIfInfoIsDropped(Name, Id, DoB, Mobile, CL, CM, Year, SD, ED):
    if Name == '' and Id == '':
        Company.nDroppentry += 1
    elif Id == '':
        Company.nDropids += 1
    elif Name == '':
        Company.nDropnames += 1
    if DoB == '':
        Company.nDropdob += 1
    if DoB != T1.modifiedDate(DoB):
        Company.nDatechange += 1
    if Mobile == '':
        Company.nDropmobiles += 1
    if CL == '':
        Company.nDropcids += 1
    if CM == '':
        Company.nDropcmake += 1
    if Year == '':
        Company.nDropcyears += 1
    if SD != T1.modifiedDate(SD):
        Company.nDatechange += 1
    if ED != T1.modifiedDate(ED):
        Company.nDatechange += 1


class Company:
    nDuplicates = 0
    nDatechange = 0
    nDropnames = 0
    nDropids = 0
    nDropdob = 0
    nDropmobiles = 0
    nDroppentry = 0
    nDropcmake = 0
    nDropcids = 0
    nDropcyears = 0

    def __init__(self):
        self.__listOfPeople = []
        self.__listOfCars = []

    def __del__(self):
        print('DataBase Will Be Removed!\n')

    def getListOfPeople(self):
        return self.__listOfPeople

    def getListOfCars(self):
        return self.__listOfCars

    def add(self, Name='', Id='', DoB='', Mobile='', CL='', CM='', Year='', SD='', ED='', RB=''):
        flag = 1
        if ((Id.isdigit() or len(Id) == 0) and (Mobile.isdigit() or len(Mobile) == 0) and (
                CL.isalnum() or len(CL) == 0) and (CM.isalpha() or len(CM) == 0) and (
                Year.isdigit() or len(Year) == 0) and (RB.isdigit() or len(RB) == 0)):
            checkIfInfoIsDropped(Name, Id, DoB, Mobile, CL, CM, Year, SD, ED)
            new = {"Name": Name, "Id": Id, "DoB": DoB, "Mobile": Mobile, "CL": CL, "CM": CM, "Year": Year,
                   "SD": SD, "ED": ED, "RB": RB}
            for obj in self.getListOfPeople():
                for rent in obj.getlistOfRents():
                    if CL == '':
                        break
                    if rent.getCL() == CL:
                        T1.fixCarInfo(rent, new)
                if Id == '':
                    break
                if obj.getId() == new["Id"]:
                    T1.fixPersonInfo(obj, new)
                    flag = 0
                    obj.addRental(new["CL"], new["CM"], new["Year"], new["SD"], new["ED"], new["RB"])
                    break
            if flag:
                self.getListOfPeople().append(
                    Person(new["Name"], new["Id"], new["DoB"], new["Mobile"], new["CL"], new["CM"],
                           new["Year"], new["SD"], new["ED"], new["RB"]))
            flag = 1
            for obj in self.getListOfCars():
                for rent in obj.getlistOfRents():
                    if Id == '':
                        break
                    if rent.getId() == Id:
                        T1.fixPersonInfo(rent, new)
                if CL == '':
                    break
                if obj.getCL() == new["CL"]:
                    T1.fixCarInfo(obj, new)
                    flag = 0
                    obj.addRental(new["Name"], new["Id"], new["DoB"], new["Mobile"], new["SD"], new["ED"], new["RB"])
                    break
            if flag:
                self.getListOfCars().append(Car(new["Name"], new["Id"], new["DoB"], new["Mobile"], new["CL"], new["CM"],
                                                new["Year"], new["SD"], new["ED"], new["RB"]))
        else:
            print("There is at least one wrong input!")


class Info:
    """Define a New Car Rental"""

    def setName(self, Name):
        self.__Name = Name

    def getName(self):
        return self.__Name

    def setId(self, Id):
        self.__Id = Id

    def getId(self):
        return self.__Id

    def setDoB(self, DoB):
        self.__DoB = T1.modifiedDate(DoB)

    def getDoB(self):
        return self.__DoB

    def setMobile(self, Mobile):
        self.__Mobile = Mobile

    def getMobile(self):
        return self.__Mobile

    def setCL(self, CL):
        self.__CL = CL

    def getCL(self):
        return self.__CL

    def setCM(self, CM):
        self.__CM = CM

    def getCM(self):
        return self.__CM

    def setYear(self, Year):
        self.__Year = Year

    def getYear(self):
        return self.__Year

    def setSD(self, SD):
        self.__SD = T1.modifiedDate(SD)

    def getSD(self):
        return self.__SD

    def setED(self, ED):
        self.__ED = T1.modifiedDate(ED)

    def getED(self):
        return self.__ED

    def setRB(self, RB):
        self.__RB = RB

    def getRB(self):
        return self.__RB


class abstractRent(Info):
    def printInfo(self):
        raise NotImplementedError("Subclass must implement abstract method")


class RentByPerson(abstractRent):

    def __init__(self, CL='', CM='', Year='', SD='', ED='', RB=''):
        self.setCL(CL)
        self.setCM(CM)
        self.setYear(Year)
        self.setSD(SD)
        self.setED(ED)
        self.setRB(RB)

    def printInfo(self):
        print(
            "  CL: " + self.getCL() + ", CM: " + self.getCM() + ", Year: " + self.getYear() + ", SD: " + self.getSD() +
            ", ED: " + self.getED() + ", RB: " + self.getRB())


class RentByCar(abstractRent):
    def __init__(self, Name='', Id='', DoB='', Mobile='', SD='', ED='', RB=''):
        self.setName(Name)
        self.setId(Id)
        self.setDoB(DoB)
        self.setMobile(Mobile)
        self.setSD(SD)
        self.setED(ED)
        self.setRB(RB)

    def printInfo(self):
        print(
            "  Name: " + self.getName() + ", Id: " + self.getId() + ", Date Of Birth: " + self.getDoB() + ", Mobile: " +
            self.getMobile() + ", SD: " + self.getSD() + ", ED: " + self.getED() + ", RB: " + self.getRB())


class abstractCategory(Info):
    def getlistOfRents(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def addRental(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def showRentals(self):
        for obj in self.getlistOfRents():
            obj.printInfo()

    def printInfo(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def calculateMoney(self):
        summation = 0
        for rent in self.getlistOfRents():
            summation += int(rent.getRB())
        return summation


class Person(abstractCategory):
    """Who rents the car"""

    def getlistOfRents(self):
        return self.__listOfRents

    def addRental(self, CL='', CM='', Year='', SD='', ED='', RB=''):
        if T1.isDuplicatedPerson(self, CL, CM, Year, SD, ED, RB):
            Company.nDuplicates += 1
            return
        self.getlistOfRents().append(RentByPerson(CL, CM, Year, SD, ED, RB))

    def __init__(self, Name='', Id='', DoB='', Mobile='', CL='', CM='', Year='', SD='', ED='', RB=''):
        self.setName(Name)
        self.setId(Id)
        self.setDoB(DoB)
        self.setMobile(Mobile)
        self.__listOfRents = []
        self.addRental(CL, CM, Year, SD, ED, RB)

    def printInfo(self):
        print(
            "* Name: " + self.getName() + ", ID: " + self.getId() + ", Date Of Birth: " + self.getDoB() + ", Mobile: " +
            self.getMobile() + " *")


class Car(abstractCategory):
    """Which be rented"""

    def getlistOfRents(self):
        return self.__listOfRents

    def addRental(self, Name='', Id='', DoB='', Mobile='', SD='', ED='', RB=''):
        if T1.isDuplicatedCar(self, Name, Id, DoB, Mobile, SD, ED, RB):
            return
        self.getlistOfRents().append(RentByCar(Name, Id, DoB, Mobile, SD, ED, RB))

    def __init__(self, Name='', Id='', DoB='', Mobile='', CL='', CM='', Year='', SD='', ED='', RB=''):
        self.setCL(CL)
        self.setCM(CM)
        self.setYear(Year)
        self.__listOfRents = []
        self.addRental(Name, Id, DoB, Mobile, SD, ED, RB)

    def printInfo(self):
        print(
            "* CL: " + self.getCL() + ", CM: " + self.getCM() + ", Year: " + self.getYear() + " *")


