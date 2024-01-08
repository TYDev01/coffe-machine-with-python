# print("Hello Tony the python programmer")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

money = 0


# TO CHECK IF THE RESOURCES IS STILL OK
# GET THE CURRENT VALUE OF THE RESOURCES
# COMPARE IT WITH THE RECENT VALUE OF RESOURCES IF THERE'S ANY CHANGES

def check_resources(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry here is not enough {items}")
            return False
    return True


def coin_process():
    """ Returns the total calculated from coins inserted."""
    print("Please pay your money joh")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.1
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Your change is {change}, here it is.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name} ☕️")


def choice_drink():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            for key, values in resources.items():
                if key == "coffee":
                    unit = "g"
                else:
                    unit = "ml"
                print(f"{key}: {values}{unit}")
            print(f"Money: ${money}")
        else:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                payment = coin_process()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffe(choice, drink["ingredients"])


choice_drink()
# TODO: 1. Check your codes https://docs.walletconnect.com/web3modal/nextjs/about.
