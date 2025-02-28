from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# TODO: 1. Print report of all coffee machine resources.
def report():
    print(f"Water  : {resources["water"]} ml")
    print(f"Milk   : {resources["milk"]} ml")
    print(f"Coffee : {resources["coffee"]} g")
    print(f"Money  : RM {"{:.2f}".format(profit)}")


# TODO: 2. Check if resources is sufficient to make drink order.
def check_resources(drink):
    for item in resources:
        if resources[item] < drink["ingredients"][item]:
            print(f"Sorry, insufficient {item}.")
            return False
    return True


# TODO: 3. Process coins.
def calculate():
    print("\nPlease insert coin.")
    quarters = float(input("How many quarters ? "))
    dimes = float(input("How many dimes ? "))
    nickels = float(input("How many nickels ? "))
    pennies = float(input("How many pennies ? "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total


# TODO: 4. Check if transaction is successful.
def check_transaction(money, drink):
    if money < drink["cost"]:
        print("Sorry, not enough money. Money refunded.")
        return False
    else:
        change = money - drink["cost"]
        print(f"\nHere is RM {"{:.2f}".format(change)} in change.")
        return True


# TODO: 5. Make coffee.
def update_resources(coffee):
    global profit
    for item in resources:
        resources[item] -= MENU[coffee]["ingredients"][item]
    print(f"\nHere is your {coffee} ☕. Enjoy !")
    profit += MENU[coffee]["cost"]



print(logo)

machine_working = True
while machine_working:
    print("\n")
    print("-------------------------------------------------------------------------------")
    choice = input("What would you like ? (espresso / latte / cappuccino) : ").lower()

    if choice == "off":
        machine_working = False
    elif choice == "report":
        report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        coffee_choice = MENU[choice]
        if check_resources(coffee_choice):
            coins = calculate()
            if check_transaction(coins, coffee_choice):
                update_resources(choice)
    else:
        print("Invalid input.")
