menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffe": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffe": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffe": 24,
        },
        "cost": 3.0,
    }
}

Water = 300
Milk = 200
Coffe = 100
Money = 0


def check_total_resources(drink):
    """Check if there are enough resources for the drink"""
    global Water, Milk, Coffe

    ingredients = menu[drink]["ingredients"]
    water_needed = ingredients.get("water", 0)
    milk_needed = ingredients.get("milk", 0)
    coffe_needed = ingredients.get("coffe", 0)

    if Water >= water_needed and Milk >= milk_needed and Coffe >= coffe_needed:
        return True
    else:
        # Show which resource is insufficient
        if Water < water_needed:
            print(f"Sorry, there is not enough water.")
        elif Milk < milk_needed:
            print(f"Sorry, there is not enough milk.")
        elif Coffe < coffe_needed:
            print(f"Sorry, there is not enough coffe.")
        return False


def update_resources(drink, cost_paid):
    """Update resources after making a drink"""
    global Water, Milk, Coffe, Money

    ingredients = menu[drink]["ingredients"]
    Water -= ingredients.get("water", 0)
    Milk -= ingredients.get("milk", 0)
    Coffe -= ingredients.get("coffe", 0)
    Money += menu[drink]["cost"]

    # Calculate and return change
    change = round(cost_paid - menu[drink]["cost"], 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    print(f"Here is your {drink}. Enjoy!")


def pay_checker(drink):
    """Check if user inserted enough money"""
    print("Please insert the money")
    quarter_count = int(input("How many quarters?: "))
    dimes_count = int(input("How many dimes?: "))
    nickles_count = int(input("How many nickles?: "))
    pennies_count = int(input("How many pennies?: "))

    total_inserted = (quarter_count * 0.25 +
                      dimes_count * 0.10 +
                      nickles_count * 0.05 +
                      pennies_count * 0.01)

    cost = menu[drink]["cost"]

    if total_inserted >= cost:
        return True, total_inserted
    else:
        print(f"Sorry, that's not enough money. You inserted ${total_inserted:.2f} but the drink costs ${cost}.")
        print("Money refunded.")
        return False, 0


# Main program loop
print("Welcome to the Coffee Machine!")
user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

while user_input != "off":
    if user_input == "report":
        print(f"\nCurrent resources:")
        print(f"Water: {Water}ml")
        print(f"Milk: {Milk}ml")
        print(f"Coffee: {Coffe}g")
        print(f"Money: ${Money}\n")

    elif user_input in ["espresso", "latte", "cappuccino"]:
        # First check if there are enough resources
        if check_total_resources(user_input):
            # Then check payment
            payment_ok, total_paid = pay_checker(user_input)

            if payment_ok:
                update_resources(user_input, total_paid)
            # If payment not OK, money is already refunded in pay_checker
    else:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")

    user_input = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

print("Coffee machine turned off. Goodbye!")
