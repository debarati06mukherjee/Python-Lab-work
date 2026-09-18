class Transport:
    def get_val(self):
        self.type = input("Enter transport type: ")


class Bus(Transport):
    def input(self):
        self.seat = int(input("Enter seat number: "))
        self.source = input("Enter source: ")
        self.destination = input("Enter destination: ")

    def show(self):
        print("Transport Type:", self.type)
        print("Seat Number:", self.seat)
        print("Source:", self.source)
        print("Destination:", self.destination)


bus = Bus()
bus.get_val()
bus.input()
bus.show()