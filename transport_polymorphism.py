class Transport:

    def __init__(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)


class Boat(Transport):

    def __init__(self, type, seat, source, destination):
        super().__init__(type)
        self.seat = seat
        self.source = source
        self.destination = destination

    def show(self):
        super().show()
        print("Seat No:", self.seat)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print()


class Bus(Transport):

    def __init__(self, type, seat, source, destination):
        super().__init__(type)
        self.seat = seat
        self.source = source
        self.destination = destination

    def show(self):
        super().show()
        print("Seat No:", self.seat)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print()


# Creating 2 Boat objects
ob1 = Boat("Water Transport - Boat", 40, "Kolkata", "Siliguri")
ob2 = Boat("Water Transport - Boat", 50, "Kolkata", "Asansol")

# Creating 2 Bus objects
ob3 = Bus("Land Transport - Bus", 30, "Kolkata", "Durgapur")
ob4 = Bus("Land Transport - Bus", 40, "Kolkata", "Asansol")


# Display Boat details
print("BOAT DETAILS")
ob1.show()
ob2.show()

# Display Bus details
print("BUS DETAILS")
ob3.show()
ob4.show()