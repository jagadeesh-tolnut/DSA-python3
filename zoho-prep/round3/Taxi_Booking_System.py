MAP = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}
TAXI = {}
DISTANCE = 15
MINIMUM_CHARGE = 100
CHARGE_PER_KILOMETER = 10


class Taxi:
    def __init__(self, no: int, pos="A", earning=0, free=True):
        self.no = no
        self.pos = pos
        self.earning = earning
        self.free = free
        self.booked_slots = []


def book(pick, drop):
    Taxi_distances = {}
    for i in TAXI:
        TAXI[i]

    for i in TAXI:
        TAXI[i]

        if TAXI[i].free:
            pass


def taxiCharge(pick, drop):
    distance = calcDistance(pick, drop)
    if distance > 5:
        return 100 + (distance - 5) * 10
    else:
        return 100

def get_taxi_distances(pick):
    avai_taxi_dis = {}
    for i in TAXI:
        if TAXI[i].free:
            distance_from_customer = abs(MAP[TAXI[i].pos] - MAP[pick])
            avai_taxi_dis.update({str(i):distance_from_customer})
    return avai_taxi_dis


def isTaxisAvailable():
    for i in TAXI:
        if TAXI[i].free:
            return True
        else:
            return False

def calcDistance(pick, drop):
    return abs(MAP[pick] - MAP[drop]) * DISTANCE




if __name__ == "__main__":
    number_of_taxis = int(input("Enter the number of taxis: "))
    for i in range(1, number_of_taxis + 1):
        TAXI[str(i)] = Taxi(i)
