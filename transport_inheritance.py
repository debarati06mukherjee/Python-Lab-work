class Transport:

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def show(self):
        print("Type:", self.type)
        print("Value:", self.value)


class Bus(Transport):

    def __init__(self, type, value, seat, source, destination):
        super().__init__(type, value)
        self.seat = seat
        self.source = source
        self.destination = destination

    def display(self):
        self.show()
        print("Seat Number:", self.seat)
        print("Source:", self.source)
        print("Destination:", self.destination)


# Creating Bus object
bus = Bus("Bus", 500, 20, "Kolkata", "Siliguri")

# Display all details
bus.display()