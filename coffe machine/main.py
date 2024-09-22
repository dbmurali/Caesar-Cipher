from resource import MENU
from resource import resources

turn_off=False



def resource_left(coffe):
    """USED TO CALCULATE THE RESOURCE LEFT REMAINING """
    total_water=resources["ingredients"]["water"]-coffe["ingredients"]["water"]
    total_milk=resources["ingredients"]["milk"]-coffe["ingredients"]["milk"]
    total_coffe=resources["ingredients"]["coffee"]-coffe["ingredients"]["coffee"]

    balance={"water":total_water,"milk":total_milk,"coffee": total_coffe}
    return balance

def bill(coffe_type,price):
    name = input("enter your name: ")
    contact = input("enter your contact number: ")
    print("#######################################################")
    print(f" name: {name}\n contact: {contact}\n cofee: {coffe_type}\n price:$ {price}\n")
    print("#######################################################")

balance={
    "water": 300,
    "coffee": 100,
    "milk": 200,
}
def report(balance,turn_off,):
    while not turn_off:


        coffe_type = input("What do you like to have: espresso/latte/cappuccino: \n").lower()
        coffe = MENU[coffe_type]
        ingredentes=coffe["ingredients"]
        if balance["coffee"]>=ingredentes["coffee"] :
            if balance["milk"]>=ingredentes["milk"] :
                if balance["water"]>=ingredentes["water"]:
                    conform=input(f"You have selected {coffe_type} and its price: ${coffe["cost"]}\n please entre \"yes\" to conform: ")
                    if conform=="yes":
                        balance=resource_left(coffe)
                        print(balance)
                        buy=input("yes for buy again and No for generate bill: ").lower()
                        if buy=="no":
                            turn_off=True
                            bill(coffe_type,coffe["cost"])
        else:
            print("insuffecent resource")


report(balance,turn_off)
