import random
import json
import time


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
    "Aquafina"    : {"price": 1.53, "stock": random.randint(0,3), "number": 4},
}

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

    while True:
        try:
            print("What would you like to buy?")
            time.sleep(1)
            itemChose = int(input("Enter Item Number(or 0 to exit)   "))
            if itemChose <1:
                Error()
            elif itemChose >12:
                Error()
            elif itemChose == 0:
                print("\nReturning to the main menu...")
                time.sleep(0.5)
                return
        except ValueError:
            Error()
            
            selectedItem = None
            for name, details in items.items(): 
                if details["number"] == itemChose:
                    selectedItem = (name, details)
            if userBalance >= selectedItem[1]["price"]:
                if selectedItem[1]["stock"] > 0:
                    userbalance = userbalance - selectedItem[1]["price"]
                    print(userBalance)
       

def main(): #Basic Choice

    
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

            else:
                Error()
                
        except ValueError:
            Error()


main()