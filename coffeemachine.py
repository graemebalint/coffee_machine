import menu

class CoffeeMachine:

    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0

    def report(self):
        self.supplies = self.machine_resources(0, 0, 0, 0)
        # print(supplies)
        print(f"Water: {self.supplies[0]}ml,\nMilk: {self.supplies[1]}ml,\nCoffee: {self.supplies[2]}g,\nMoney: ${self.supplies[3]}")

    def machine_resources(self, a, b, c, d):
        self.money = 0

        self.water -= a
        self.milk -= b
        self.coffee -= c
        self.money += d
        return [self.water, self.milk, self.coffee, self.money]

    def machine_refill(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0

    def make_drink(self):
        choice = input("What would you like? (latte, espresso, cappuccino)\n")

        def check_supplies(drink):
            #  enough_supplies = True
            self.available_supplies = self.machine_resources(0, 0, 0, 0)
            self.required_supplies = []
            self.required_supplies.extend([menu.MENU[drink]["ingredients"]["water"], menu.MENU[drink]["ingredients"]["milk"],
                                      menu.MENU[drink]["ingredients"]["coffee"], menu.MENU[drink]["cost"]])

            print(f"available_supplies: {self.available_supplies}")
            print(f"required_supplies: {self.required_supplies}")

            if (self.available_supplies[0] - self.required_supplies[0] < 0) or (
                    self.available_supplies[1] - self.required_supplies[1] < 0) or (
                    self.available_supplies[2] - self.required_supplies[2] < 0):
                print("Sorry, there aren't enough supplies to make that drink.")
            else:
                print(f"A {drink} costs {self.required_supplies[3]}")
                dollar_bills = float(input("# one dollar bills: "))
                quarters = float(input("# quarters: "))
                dimes = float(input("# dimes: "))

                payment = (dollar_bills * 1) + (quarters * 0.25) + (dimes * 0.1)
                remaining_payment = self.required_supplies[3] - payment

                if payment >= self.required_supplies[3]:
                    change = round((payment - self.required_supplies[3]), 2)
                    self.machine_resources(menu.MENU[drink]["ingredients"]["water"], menu.MENU[drink]["ingredients"]["milk"],
                                      menu.MENU[drink]["ingredients"]["coffee"], 0)
                    print(f"Here is your {drink}. You get ${change} in change.")
                else:
                    # remaining_payment = supplies[3] - payment
                    owing = True
                    while owing == True:
                        print(
                            f"1 {drink} costs: ${self.required_supplies[3]}\nCurrent balance: ${payment}\nPlease insert another ${remaining_payment}.")

                        dollar_bills = float(input("# one dollar bills: "))
                        quarters = float(input("# quarters: "))
                        dimes = float(input("# dimes: "))

                        payment += round(((dollar_bills * 1) + (quarters * 0.25) + (dimes * 0.1)), 2)
                        remaining_payment = round((self.required_supplies[3] - payment), 2)

                        if remaining_payment <= 0:
                            owing = False
                            change = round((payment - self.required_supplies[3]), 2)
                            print(f"Here is your {drink}. You get ${change} in change.")

        # ESPRESSO
        if choice == "espresso":
            check_supplies("espresso")
            self.make_drink()

        # LATTE
        elif choice == "latte":
            check_supplies("latte")
            self.make_drink()

        # CAPPUCCINO
        elif choice == "cappuccino":
            check_supplies("cappuccino")
            self.make_drink()

        # REPORT
        elif choice == "report":
            self.report()
            self.make_drink()

        elif choice == "off":
            print("Going to sleep. Goodnight")

        elif choice == "refill":
            self.machine_refill()
            self.make_drink()

        else:
            print("Sorry, I don't understand that input.")
            self.make_drink()