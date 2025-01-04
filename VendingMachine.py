import random

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

userBalance = user_balance = round(random.uniform(5, 10), 2)

print("Welcome to the AutoSnack Vending Machine!")
print("Here is how much money you have:  $",userBalance )