import datetime


def carStatistics(company):
    for car in company.getListOfCars():
        car.printInfo()
        print("   Number of days the car was rented: " + str(calculateRentedDays(car)) +
              "\n The Revenue Made By Renting This Car: " + str(car.calculateMoney()) +
              "\nAverage price per day for renting each car: " + str(car.calculateMoney() / calculateRentedDays(car)))


def calculateRentedDays(self):
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
              "September": 9, "October": 10, "November": 11, "December": 12}
    summation = 0
    for rent in self.getlistOfRents():
        SDcols = rent.getSD().split(" ")
        EDcols = rent.getED().split(" ")
        summation += int((
                                 datetime.date(int(EDcols[2]), months[EDcols[1]], int(EDcols[0])) -
                                 datetime.date(int(SDcols[2]), months[SDcols[1]], int(SDcols[0]))).days)
        del SDcols
        del EDcols
    return summation
