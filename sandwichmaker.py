import pyinputplus as pyip

# Define the prices for each ingredient
BREAD_PRICES = {
    "wheat": 1.50,
    "white": 1.25,
    "sourdough": 1.75
}

PROTEIN_PRICES = {
    "chicken": 2.00,
    "turkey": 2.25,
    "ham": 1.75,
    "tofu": 1.50
}

CHEESE_PRICES = {
    "cheddar": 0.50,
    "swiss": 0.75,
    "mozzarella": 0.60,
    "none": 0
}

TOPPING_PRICES = {
    "mayo": 0.20,
    "mustard": 0.15,
    "lettuce": 0.10,
    "tomato": 0.20
}

def get_sandwich_order():
    bread_type = pyip.inputMenu(list(BREAD_PRICES.keys()), prompt="Choose a bread type: ")
    protein_type = pyip.inputMenu(list(PROTEIN_PRICES.keys()), prompt="Choose a protein type: ")
    wants_cheese = pyip.inputYesNo("Do you want cheese? ")
    if wants_cheese:
        cheese_type = pyip.inputMenu(list(CHEESE_PRICES.keys()), prompt="Choose a cheese type: ")
    else:
        cheese_type = None
    toppings = []
    for topping in TOPPING_PRICES.keys():
        if pyip.inputYesNo(f"Do you want {topping}? "):
            toppings.append(topping)
    num_sandwiches = pyip.inputInt("How many sandwiches do you want? ", min=1)
    return {
        "bread_type": bread_type,
        "protein_type": protein_type,
        "cheese_type": cheese_type,
        "toppings": toppings,
        "num_sandwiches": num_sandwiches
    }

def calculate_total_cost(order):
    total_cost = BREAD_PRICES[order["bread_type"]] + PROTEIN_PRICES[order["protein_type"]]
    if order["cheese_type"]:
        total_cost += CHEESE_PRICES[order["cheese_type"]]
    for topping in order["toppings"]:
        total_cost += TOPPING_PRICES[topping]
    total_cost *= order["num_sandwiches"]
    return total_cost

def main():
    order = get_sandwich_order()
    total_cost = calculate_total_cost(order)
    print(f"Your order is:")
    print(f"- {order['num_sandwiches']} sandwich(es) with {order['bread_type']} bread, {order['protein_type']} protein, {', '.join(order['toppings'])}")
    if order['cheese_type']:
        print(f"and {order['cheese_type']} cheese")
    print(f"The total cost is ${total_cost:.2f}")

if __name__ == "__main__":
    main()