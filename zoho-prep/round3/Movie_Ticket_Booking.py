class TheaterTicket:
    FIRSTCLASS = 2
    SECONDCLASS = 2
    THIRDCLASS = 2

    def __init__(self):
        pass

    @classmethod
    def availableTickets(cls):
        return TheaterTicket.FIRSTCLASS + TheaterTicket.SECONDCLASS + TheaterTicket.THIRDCLASS

    def isTicketAvailable(self):
        return True if self.availableTickets() > 0 else False

    def bookTicket(self,pref):
        if self.isPrefAvailable(pref):
            match pref:
                case "F":
                    self.bookFistClass()

                case "S":
                    self.bookSecondClass()

                case "T":
                    self.bookThirdClass()

                case "default":
                    print("Enter a valid preference")
        else:
            match pref:
                case "F":
                    if self.isPrefAvailable("S"):
                        self.bookSecondClass()
                    elif self.isPrefAvailable("T"):
                        self.bookThirdClass()
                    else:
                        print("No Tickets Available Now")

                case "S":
                    if self.isPrefAvailable("F"):
                        self.bookSecondClass()
                    elif self.isPrefAvailable("T"):
                        self.bookThirdClass()
                    else:
                        print("No Tickets Available Now")

                case "T":
                    if self.isPrefAvailable("S"):
                        self.bookSecondClass()
                    elif self.isPrefAvailable("F"):
                        self.bookThirdClass()
                    else:
                        print("No Tickets Available Now")

                case "default":
                    print("Enter a valid preference")

    def cancelTicket(self,pref):
        match pref:
            case "F":
                TheaterTicket.FIRSTCLASS += 1

            case "S":
                TheaterTicket.SECONDCLASS += 1

            case "T":
                TheaterTicket.THIRDCLASS += 1

            case "default":
                print("Enter a valid preference")


    def isPrefAvailable(self,pref):
        match pref:
            case "F":
                return True if TheaterTicket.FIRSTCLASS > 0 else False

            case "S":
                return True if TheaterTicket.SECONDCLASS > 0 else False

            case "T":
                return True if TheaterTicket.THIRDCLASS > 0 else False

            case "default":
                print("Enter a valid preference")

    def bookFistClass(self):
        TheaterTicket.FIRSTCLASS -= 1

    def bookSecondClass(self):
        TheaterTicket.SECONDCLASS -= 1

    def bookThirdClass(self):
        TheaterTicket.THIRDCLASS -= 1

    def printAvailableTickets(self):
        print("Availabe tickets are: ")
        print("Firstclass- "+str(TheaterTicket.FIRSTCLASS))
        print("Secondclass- "+str(TheaterTicket.SECONDCLASS))
        print("Thirdclass- "+str(TheaterTicket.THIRDCLASS))
        print()

    # def printBookedTickets(self):
    #     print("Availabe tickets are: ")
    #     print("Firstclass- "+str(TheaterTicket.FIRSTCLASS))
    #     print("Secondclass- "+str(TheaterTicket.SECONDCLASS))
    #     print("Thirdclass- "+str(TheaterTicket.THIRDCLASS))
    #     print()



if __name__ == "__main__":

    t1 = TheaterTicket()
    print("******Welcome To Ticket Booking App*******")

    while(True):
        print("Your choices :")
        print("1 - Book Ticket")
        print("2 - Cancel Ticket")
        print("3 - Veiw Available Tickets")
        # print("4 - Veiw Booked Tickets")
        print("0 - Exit App")
        choice = int(input("Enter your choice"))

        match choice:
            case 1:
                print("Ticket choices")
                print("F - Firstclass")
                print("S - Seconclass")
                print("T - Thirdclass")
                pref = input("Enter Your Preference")
                t1.bookTicket(pref)

            case 2:
                pref = input("Your booked ticket class: ")
                t1.cancelTicket(pref)

            case 3:
                t1.printAvailableTickets()

            case 0:
                break

            case "default":
                print("Enter a proper input")

