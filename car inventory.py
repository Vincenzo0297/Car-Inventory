class car:
    Insurance = 0.02

    def __init__(self, code, price, quantity):
        self.code = code
        self.price = price
        self.quantity = quantity

    def getCode(self):
        return self.code
    def getPrice(self):
        return self.price
    def getQuantity(self):
        return self.quantity
    
    def getTotal(self):
        return self.price * self.quantity

    def getInsurance(self):
        return self.getTotal() * car.Insurance
    
    def __str__(self):
        return f"Code: {self.getCode()}, Total Cost: ${self.getTotal():.2f}, Insurance: ${self.getInsurance():.2f}"
    

class carElect(car):  # Extended
    Insurance2 = 0.10

    def __init__(self, code, price, quantity, battery_duration, charge_duration):
        super().__init__(code, price, quantity)
        self.battery_duration = battery_duration
        self.charge_duration = charge_duration

    def getBatteryDuration(self):
        return self.battery_duration

    def getChargeDuration(self):
        return self.charge_duration

    def getTotal(self):
        return self.getPrice() * self.getQuantity()  # Use self here to access instance methods

    def getInsurance(self):
        return self.getTotal() * carElect.Insurance2

    def __str__(self):
        return super().__str__() + f", Battery Duration: {self.battery_duration} mins, Charge Duration: {self.charge_duration} mins"

def main(inventory_list):
    while True:
        print("\n1 Add inventory")
        print("2 Remove inventory")
        print("3 Show all inventory")
        print("4 Search inventory by car model")
        print("5 Search inventory by car price")
        print("6 Search inventory by car battery duration")
        print("7 Quit")
        choice = input("Your selection: ")
        
        if choice == "1":
            add_inventory(inventory_list)
        elif choice == "2":
            remove_inventory(inventory_list)
        elif choice == "3":
            display_all(inventory_list)
        elif choice == "4":
            search_inventory(inventory_list)
        elif choice == "5":
            search_by_price(inventory_list)
        elif choice == "6":
            search_by_battery_duration(inventory_list)
        elif choice == "7":
            print("Quit")
            break
        else:
            print("Invalid option. Please try again.")
    

def add_inventory(inventory_list):
    while True:
        try:
            code = input("Code: ")
            if any(item.getCode() == code for item in inventory_list):
                print("Same Code")
                break

            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            if price < 0 or quantity < 0:
                print("No Negative Number")
                break

            battery = input("Does it have a Battery (y/n)? ").lower()
            if battery == "y":
                battery_duration = float(input("Battery Duration fully Charge in Mins: "))
                if battery_duration < 0:
                    print("No Negative Number")
                    break

                charge_duration = float(input("How long it takes to Charge in Mins? "))
                if charge_duration < 0:
                    print("No Negative Number")
                    break

                inventory_list.append(carElect(code, price, quantity, battery_duration, charge_duration))
            else:
                inventory_list.append(car(code, price, quantity))
            break

        except ValueError:
            print("Invalid input. Please enter the correct values.")


def remove_inventory(inventory_list):
    code = input("Remove Model: ")
    for item in inventory_list:
        if item.getCode() == code:
            inventory_list.remove(item)
            print("Model has been removed")
            return
    print("Invalid Model")


def display_all(inventory_list):
    if not inventory_list:
        print("Invalid: No Inventory available")
    for item in inventory_list:
        print(item)


def search_inventory(inventory_list):
    code = input("Search Car Model: ")
    for item in inventory_list:
        if item.getCode() == code:
            print(item)
            return
    print("Car Model Not Found")


def search_by_price(inventory_list):
    try:
        lower_bound = float(input("Lower Bound: "))
        upper_bound = float(input("Upper Bound: "))
        if lower_bound < 0 or upper_bound < 0:
            print("Can't be negative")
            return

        found = False
        for item in inventory_list:
            if lower_bound <= item.getTotal() <= upper_bound:
                print(item)
                found = True

        if not found:
            print("No matching prices found!!!")

    except ValueError:
        print("Re-enter Number again")


def search_by_battery_duration(inventory_list):
    try:
        battery_minimum = float(input("Battery Minimum in Mins: "))
        if battery_minimum < 0:
            print("No Negative Number")
            return

        found = False
        for item in inventory_list:
            if isinstance(item, carElect) and item.getBatteryDuration() >= battery_minimum:
                print(item)
                found = True

        if not found:
            print("No duration found")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Main program entry point
if __name__ == "__main__":
    inventory_list = []
    main(inventory_list)
