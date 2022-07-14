import Task1 as T1
import datetime


def newCarRental(company):
    dictionary = {'Name: ': '', 'Id: ': '', 'Date Of Birth: ': '', 'Mobile: ': '', 'Car Rent Start Date: ': '',
                  'Car Rent End Date: ': ''}
    listOfAvailableCars = []
    for element in dictionary.keys():
        dictionary[element] = input(element)
    for car in company.getListOfCars():
        if isAvailable(car, dictionary["Car Rent Start Date: "], dictionary["Car Rent End Date: "]):
            listOfAvailableCars.append(car)
    i = 0
    for car in listOfAvailableCars:
        i += 1
        print("*" + str(i), end="")
        car.printInfo()
    if i == 0:
        print("No Available Cars During These Days, Sorry!\n")
        return
    WantedCar = input("Enter The Number Of Car That You Want: ")
    WantedCar = int(WantedCar) - 1
    RB = input("The Amount Paid For This Rental: ")
    company.add(dictionary["Name: "], dictionary["Id: "], dictionary["Date Of Birth: "], dictionary["Mobile: "],
                listOfAvailableCars[WantedCar].getCL(), listOfAvailableCars[WantedCar].getCM(),
                listOfAvailableCars[WantedCar].getYear(), dictionary["Car Rent Start Date: "],
                dictionary["Car Rent End Date: "],
                RB)
    T1.moveDataBase(company)
    print("The Car Rental Was Added!")


def isAvailable(self, WantedSD, WantedED):
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
              "September": 9, "October": 10, "November": 11, "December": 12}
    WantedSDcols = T1.modifiedDate(WantedSD).split(" ")
    WantedEDcols = T1.modifiedDate(WantedED).split(" ")
    for rent in self.getlistOfRents():
        SDcols = rent.getSD().split(" ")
        EDcols = rent.getED().split(" ")
        if (datetime.date(int(EDcols[2]), months[EDcols[1]], int(EDcols[0])) >=
            datetime.date(int(WantedSDcols[2]), months[WantedSDcols[1]], int(WantedSDcols[0])) >=
            datetime.date(int(SDcols[2]), months[SDcols[1]], int(SDcols[0]))) or \
                (datetime.date(int(EDcols[2]), months[EDcols[1]], int(EDcols[0])) >=
                 (datetime.date(int(WantedEDcols[2]), months[WantedEDcols[1]], int(WantedEDcols[0]))) >=
                 datetime.date(int(SDcols[2]), months[SDcols[1]], int(SDcols[0]))):
            return 0
    return 1
