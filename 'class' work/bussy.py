class Metro:
    bus_list = []

    def __init__(self, bus_number, bus_route, bus_driver):
        self.bus_number = bus_number
        self.bus_route = bus_route
        self.bus_driver = bus_driver
        Metro.bus_list.append(self)

    def display_info(self):
        for bus in Metro.bus_list:
            if bus == self:
                print(f"Bus number is {bus.bus_number} on Route is {bus.bus_route} and driver is {bus.bus_driver}")


def find_bus(question):
    bus_to_find = input(question)
    for bus in Metro.bus_list:
        if bus_to_find == str(bus.bus_number):
            return Metro.display_info(bus)
    print(f"Bus {bus_to_find} is not registered on the system yet.")


bus1 = Metro(3051, "Blue", "Greg")
bus2 = Metro(1940, "Red", "Dorris")
bus3 = Metro(8965, 195, "Bethany")


find_bus("Which bus number do you want (ex. '1234'): ")
