#THIS IS GOOD CODE: INCASE main.py GETS DELETED

from menu import MENU, resources

total_money = 0.00
print(total_money)
global make_drink
make_drink = True #FLAG

"===================================================="
def choice(): #1
    global user_drink
    user_drink = input("What would you like? (espresso/latte/cappuccino): ")
    if user_drink == 'report':
        report()

    for i in MENU:  # for key in dict MENU, eg: esp, lat, cap
        if i == user_drink:  # for the key that is the same as user input choice ("drink" -> choice())
            print(MENU[i], '/// choice()')
            return MENU[i]  # return nested dicts 'ingrediants' and 'cost'

"===================================================="

def money_count(): #2
    global total_money
    quar = (quarters*0.25)
    dim = (dimes*0.10)
    nic = (nickles*0.05)
    pen = (pennies*0.01)

    total_money += round(quar + dim + nic + pen, 2)
    return total_money

"===================================================="

def get_ingr(drink_spec):
    for i in drink_spec:
        if i == 'ingredients':
            ingrs = drink_spec[i]
            print(ingrs, "/// get_ingr()")
            return ingrs

"----------------------------------------------------"

def get_price(drink_spec):
    for i in drink_spec:
        if i == 'cost':
            price = drink_spec[i]
            print(price, "/// get_price()")
            return price

"===================================================="

def compare(ingredient): #3
    global make_drink; True

    for i in ingredient:
        if i == 'water':
            water_amt = ingredient[i]
            print(water_amt, "/// water() needed")

    a = resources.get('water')
    print(a, "water have")
    if water_amt > a:
        print(f"current milk: {a}, need {water_amt}")
        make_drink = False
    else:
        for i in resources:
            if i == 'water':
                q = (resources[i] - water_amt)
                resources.update({'water': q})
                print(resources[i], "water left") #amount water left
            make_drink = True
    "----------------------------------------------------"
    for i in ingredient:
        if i == 'milk':
            milk_amt = ingredient[i]
            print(milk_amt, "/// milk() needed")

    b = resources.get('milk')
    print(b, 'milk have')
    if milk_amt > b:
        print(f"current milk: {b}, need {milk_amt}")
        make_drink = False
    else:
        for i in resources:
            if i == 'milk':
                q = (resources[i] - milk_amt)
                resources.update({'milk': q})
                print(resources[i], "milk left")
            make_drink = True
    "----------------------------------------------------"

    for i in ingredient:
        if i == 'coffee':
            coffee_amt = ingredient[i]
            print(coffee_amt, "/// coffee() needed")

    c = resources.get('coffee')
    print(c, 'coffee have')
    if coffee_amt > c:
        print(f"current coffee: {c}, need {coffee_amt}")
        make_drink = False
    else:
        for i in resources:
            if i == 'coffee':
                q = (resources[i] - coffee_amt)
                resources.update({'coffee': q})
                print(resources[i], "coffee left")
                make_drink = True

"===================================================="
def compare_e(ingredient): #3.5
    global make_drink
    make_drink = True

    for i in ingredient:
        if i == 'water':
            water_amt = ingredient[i]
            print(water_amt, "/// water()")

    a = resources.get('water')
    if water_amt > a:
        print(f"current milk: {a}, need {water_amt}")
        make_drink = False
    else:
        for i in resources:
            if i == 'water':
                resources[i] -= water_amt
                print(resources[i], "waterr") #amount water left
            make_drink = True
    "----------------------------------------------------"

    for i in ingredient:
        if i == 'coffee':
            coffee_amt = ingredient[i]
            print(coffee_amt, "/// coffee()")

    c = resources.get('coffee')
    print(c)
    if coffee_amt > c:
        print(f"current coffee: {c}, need {coffee_amt}")
        make_drink = False
    else:
        for i in resources:
            if i == 'coffee':
                resources[i] -= coffee_amt
                print(resources[i], "coffeee")
                make_drink = True

"===================================================="

def report(): #USER REQUEST
    global total_money
    global make_drink
    print(resources)
    print(total_money)
    make_drink = False

"===================================================="

def comp_cost():
    global x
    global make_drink; True
    global total_money
    global d

    d = total_money

    if get_price(x) > d:
        print(f"price for drink is {get_price(x)}, you inserted {d} /// comp_cost()")
        total_money = 0 #need to make sure money is defined and matched (maybe global)
        make_drink = False #FLAG
    else:
        rest = round(d - get_price(x), 2)
        total_money = 0
        print(f"Here is your ${rest} back in change /// comp_cost()")
        make_drink = True #should set up loop so thing keeps going f enough money #FLAG

"===================================================="

"++++++++++++++++++++++++++++++++++++++++++++++++++"

while make_drink:
    global user_drink
    x = choice()
    if user_drink == "report":
        make_drink = False
        break
    if user_drink == 'espresso':
        compare_e(get_ingr(x))
    else:
        compare(get_ingr(x))

    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    money_count()
    comp_cost()
    if make_drink == False:
        print("ended")
    else:
        print(f"enjoy your {user_drink}")

"++++++++++++++++++++++++++++++++++++++++++++++++++"
