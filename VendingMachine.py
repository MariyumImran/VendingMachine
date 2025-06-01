import random
import json
import time

Items = "2"
Item2 = "out"
Item3 = "out"
Item4 = "out"
Item5 = "out"
Item6 = "out"
Item7 = "out"
Item8 = "out"
Item9 = "out"
Item10 = "out"
Item11 = "out"
Item12 = "out"
Item13 = "out"
Item14 = "out"
Item15 = "out"
Item16 = "out"

itemsPurchased = {

    "Pringles"    : {"purchasedQuantity": 0},
    "Lays"        : {"purchasedQuantity": 0},
    "Cheetos"     : {"purchasedQuantity": 0},
    "Takis"       : {"purchasedQuantity": 0},
    "Mars"        : {"purchasedQuantity": 0},
    "Hershey"     : {"purchasedQuantity": 0},
    "M&Ms"        : {"purchasedQuantity": 0},
    "Kit Kat"     : {"purchasedQuantity": 0},
    "Pepsi"       : {"purchasedQuantity": 0},
    "Orange Juice": {"purchasedQuantity": 0},
    "Red Bull"    : {"purchasedQuantity": 0},
    "Aquafina"    : {"purchasedQuantity": 0}
}


items = {

    "Pringles"    : {"price": 1.08, "stock": random.randint(0,3), "number": 3},
    "Lays"        : {"price": 1.38, "stock": random.randint(0,3), "number": 2},
    "Cheetos"     : {"price": 1.40, "stock": random.randint(0,3), "number": 12},
    "Takis"       : {"price": 1.17, "stock": random.randint(0,3), "number": 10},
    "Mars"        : {"price": 1.04, "stock": random.randint(0,3), "number": 6},
    "Hershey"     : {"price": 1.70, "stock": random.randint(0,3), "number": 7},
    "M&Ms"        : {"price": 1.58, "stock": random.randint(0,3), "number": 1},
    "Kit Kat"     : {"price": 1.08, "stock": random.randint(0,3), "number": 11},
    "Pepsi"       : {"price": 1.84, "stock": random.randint(0,3), "number": 9},
    "Orange Juice": {"price": 1.77, "stock": random.randint(0,3), "number": 5},
    "Red Bull"    : {"price": 2.34, "stock": random.randint(0,3), "number": 8},
    "Aquafina"    : {"price": 1.53, "stock": random.randint(0,3), "number": 4}
}

global userBalance
userBalance = round(random.uniform(5, 10), 2)
print("Welcome to the AutoSnack Vending Machine!")

def VM(): #View Menu
    print("\n    --- Available Items ---")
    print(f"{'Number':<7} {'Item':<12} {'Price':<6} {'Stock':<5}")
    print("-" * 35)
    for name, details in items.items():
        print(f"{details['number']:<7} {name:<12} ${details['price']:<6.2f} {details['stock']:<5}")
        print("-" * 35)

def Error(): #Invalid
    time.sleep(0.5)
    print("Invalid Choice, please try again")

def Exit():
    time.sleep(0.5)
    print("Exiting, come back soon!")

def VB(): #View Balance
    time.sleep(1)
    print("Here is how much money you have:  $",userBalance )

def Buy():

    global userBalance
    while True:
        try:
            print("\nWhat would you like to buy?")
            time.sleep(1)
            itemChose = int(input("Enter Item Number(or 0 to exit)   "))
            if itemChose == 0:
                print("\nReturning to the main menu...")
                time.sleep(0.5)
                return
            #elif itemChose >12:
            #    Error()
            elif itemChose <1 or itemChose >12:
                Error()
                    
            selectedItem = None
            for name, details in items.items(): 
                if details["number"] == itemChose:
                    selectedItem = (name, details)
                    break

            if userBalance > selectedItem[1]["price"]:
                if selectedItem[1]["stock"] > 0:

                    itemsPurchased[selectedItem[0]]['purchasedQuantity']+=1
                                           
                    userBalance = userBalance - selectedItem[1]["price"]
                    selectedItem[1]["stock"] = selectedItem[1]["stock"] -1
                    print("\nYou have sucessfully purchased", selectedItem[0], "for", selectedItem[1]["price"], "dollars")
                    break
                else:
                    print("Sorry, this item is out of stock")
            else:
                print("You cannot afford this item")

        except ValueError:
            Error()   

def BC(): #Basic Choice

    
    while True:
        time.sleep(1)
        print("\nWhat would you like to do?")
        time.sleep(0.5)
        print("1. Buy Something")
        time.sleep(0.5)
        print("2. Exit")
        time.sleep(0.5)
        print("3. View Menu")
        time.sleep(0.5)
        print("4. View Blance")
        time.sleep(0.5)
        
        try:

            basicChoice = int(input("Enter your choice:   "))

            if basicChoice == 1:
                Buy()

            elif basicChoice == 2:
                Exit()
                break

            elif basicChoice == 3:
                VM()

            elif basicChoice == 4:
                VB()

            elif basicChoice == 5:
                VI()

            else:
                Error()
                
        except ValueError:
            Error()

def VI(): #View Inventory

    for item in itemsPurchased:

        print("You have",item[]['purchasedQuantity'])
    



BC()