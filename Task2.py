def inquiryPerson(company):
    mode = input("a. Inquiry Using Name\tb. Inquiry Using ID\n")
    if mode == 'a':
        wantedName = input("Write the name:\n")
        wantedId = ''
    elif mode == 'b':
        wantedName = ''
        wantedId = input("Write the id:\n")
    else:
        print("Wrong Input!\n")
        return
    flag = 1
    for person in company.getListOfPeople():
        if (person.getName().lower() == wantedName.lower() and mode == 'a') or (
                person.getId() == wantedId and mode == 'b'):
            flag = 0
            person.printInfo()
            person.showRentals()
            print("   The Amount Paid By This Person For Renting Cars: " + str(person.calculateMoney()))
            break
    if flag:
        print("No Person With This Name/ID!\n")


def inquiryCar(company):
    cl = input("Write the CL:\n")
    flag = 1
    for car in company.getListOfCars():
        if car.getCL().lower() == cl.lower():
            flag = 0
            car.printInfo()
            car.showRentals()
            print("   The Revenue Made By Renting This Car: " + str(car.calculateMoney()))
            break
    if flag:
        print("No Car with this CL!\n")
