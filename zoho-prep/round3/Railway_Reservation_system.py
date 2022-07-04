class TicketBook():
    upper_berth = 2
    mid_berth = 2
    low_berth = 2
    rac = 2
    rac_queue = []
    wait = 2
    wait_queue = []

    def bookTicket(self, pref):
        if TicketBook.availabeTickets():
            if self.isTicketAvailable(pref):
                if pref == 1:
                    TicketBook.upper_berth -= 1
                    print("Upper Berth Booked")
                elif pref == 2:
                    TicketBook.mid_berth -= 1
                    print("Mid Berth Booked")
                elif pref == 3:
                    TicketBook.low_berth -= 1
                    print("Lower Berth Booked")

            else:
                if pref == 1:
                    if self.isTicketAvailable(2):
                        TicketBook.mid_berth -= 1
                        print("Mid Berth Booked")
                    elif self.isTicketAvailable(3):
                        TicketBook.low_berth -= 1
                        print("Low Berth Booked")
                    else:
                        if TicketBook.isRacAvailabe():
                            TicketBook.rac -= 1
                            print("RAC Booked")
                        elif TicketBook.isWaitAvailable():
                            TicketBook.wait -= 1
                            print("Under Waiting list")
                        else:
                            print("No Tickets Available")

                elif pref == 2:
                    if self.isTicketAvailable(1):
                        TicketBook.upper_berth -= 1
                        print("Upper Berth Booked")
                    elif self.isTicketAvailable(3):
                        TicketBook.low_berth -= 1
                        print("Lower Berth Booked")
                    else:
                        self.bookRacOrWait()

                elif pref == 3:
                    if self.isTicketAvailable(2):
                        TicketBook.mid_berth -= 2
                        print("Mid Berth Booked")
                    elif self.isTicketAvailable(1):
                        TicketBook.upper_berth -= 1
                        print("Upper Berth Booked")
                    else:
                        self.bookRacOrWait()

        else:
            self.bookRacOrWait()

    @classmethod
    def anythingAvailable(cls):
        if TicketBook.availabeTickets() + TicketBook.availabeRAC() + TicketBook.availableWaitlist():
            return True
        else:
            return False

    @staticmethod
    def availabeTickets():
        return TicketBook.upper_berth + TicketBook.mid_berth + TicketBook.low_berth

    @staticmethod
    def availabeRAC():
        return TicketBook.rac

    @staticmethod
    def availableWaitlist():
        return TicketBook.wait

    def isTicketAvailable(self, pref):
        if pref == 1:
            return True if TicketBook.upper_berth > 0 else False
        elif pref == 2:
            return True if TicketBook.mid_berth > 0 else False
        elif pref == 3:
            return True if TicketBook.low_berth > 0 else False
        else:
            return "UA"

    def bookRacOrWait(self):
        if self.isRacAvailabe():
            TicketBook.rac -= 1
            print("RAC Booked")
        elif self.isWaitAvailable():
            TicketBook.wait -= 1
            print("Under Waiting list")
        else:
            print("No Tickets Available")

    def isRacAvailabe(self):
        return True if TicketBook.rac > 0 else False

    def isWaitAvailable(self):
        return True if TicketBook.wait > 0 else False


class Customer():
    all = []

    def __init__(self, name: str, age: int, gender: int, berth: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.berth = berth
        Customer.all.append(self)


if __name__ == "__main__":
    # tick = TicketBook()
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)
    # tick.bookTicket(1)

    ticket = TicketBook()
    customer_details = {}
    customer_code = 1
    code = 1


    def add_user():
        global customer_code
        user_id = "U" + str(customer_code)
        if ticket.anythingAvailable():
            cus_name = input("Name: ")
            cus_age = int(input("Age: "))
            cus_gender = int(input("Gender(1-Male, 2-Female, 3-Transgender): "))
            cus_pref = int(input("Preference(1-Upper, 2-Middle, 3-Lower): "))
            customer_details[user_id] = Customer(cus_name, cus_age, cus_gender, cus_pref)
            ticket.bookTicket(cus_pref)

            customer_code += 1

        else:
            print("Ticket Not Available")


    while (code != 0):
        print("Available Codes ")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View Booked Tickets")
        print("0. Exit Program\n")

        code = input("Enter the input: ")

        match code:
            case "1":
                no = int(input("Enter the number of Person: "))
                for i in range(no):
                    add_user()

            case "2":
                pass
            case "3":
                print(customer_details)
            case "0":
                break
            case default:
                print("\n*** Enter a proper input ***\n")
