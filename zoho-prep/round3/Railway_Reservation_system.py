class CustomerBook():
    upper_berth = 2
    mid_berth = 2
    low_berth = 2

    def __int__(self,name: str, age: int, gender: int, berth: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.berth = berth

    def bookTicket(self,pref):
        if CustomerBook.availabeTickets():
            if self.isPrefAvailable(pref):



    @staticmethod
    def availabeTickets():
        return CustomerBook.upper_berth + CustomerBook.mid_berth + CustomerBook.low_berth

    def isPrefAvailable(self,pref):
        if pref == 1:
            return True if CustomerBook.upper_berth > 0 else False
        elif pref == 2:
            return True if CustomerBook.mid_berth > 0 else False
        elif pref == 3:
            return True if CustomerBook.mid_berth > 0 else False
        else:
            return "UA"


class Train():
    pass