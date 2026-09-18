class Transport:
    def __init__(self, type):
        self.type = type


class Boat(Transport):
    def __init__(self, type, capacity, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
        print(f"Details: {self.type}, {self.capacity}, {self.source}, {self.destination}")


class Bus(Transport):
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def show(self):
        print(f"Values: {self.type}, {self.seat_no}, {self.source}, {self.destination}")


bo1 = Boat("Boat", 28, "Kolkata", "Howrah")
bo2 = Boat("Boat", 25, "Howrah", "Kolkata")

bo1.show()
bo2.show()

bu1 = Bus("Bus", 45, "Barasat", "Bongaon")
bu2 = Bus("Bus", 40, "Barasat", "Neuit...")

bu1.show()
bu2.show()