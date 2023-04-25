from menu import MENU, resources
"===================================================="
def choice(): #1
    user_drink = input("What would you like? (espresso/latte/cappuccino): ")
    for i in MENU:  # for key in dict MENU, eg: esp, lat, cap
        if i == user_drink:  # for the key that is the same as user input choice ("drink" -> choice())
            print(MENU[i], '/// choice()')
            return MENU[i]  # return nested dicts 'ingrediants' and 'cost'

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
def water(ingredient):
    for i in ingredient:
        if i == 'water':
            water_amt = ingredient[i]
            print(water_amt, "/// water()")

    a = resources.get('water')
    if water_amt > a:
        print(f"current milk: {a}, need {water_amt}")
    else:
        return True

"----------------------------------------------------"

def milk(ingredient):
    for i in ingredient:
        if i == 'milk':
            milk_amt = ingredient[i]
            print(milk_amt, "/// milk()")

    b = resources.get('milk')
    if milk_amt > b:
        print(f"current milk: {b}, need {milk_amt}")
    else:
        return True

"----------------------------------------------------"

def coffee(ingredient):
    for i in ingredient:
        if i == 'coffee':
            coffee_amt = ingredient[i]
            print(coffee_amt, "/// coffee()")

    c = resources.get('coffee')
    if coffee_amt > c:
        print(f"current coffee: {c}, need {coffee_amt}")
    else:
        return True

"===================================================="

def comp_cost(price):
    d = "total_money"
    if get_price < d:
        print(f"price for drink is {get_price}, you inserted {d}")
        money = 0 #need to make sure money is defined and matched (maybe global)
        make_drink = False #FLAG
    else:
        make_drink = True #should set up loop so thing keeps going f enough money #FLAG

"===================================================="

def compare(wat, mil, cof): #3
    if wat == True:
        make_drink = True
    else:
        print("not enough water")
        make_drink = False
    if mil == True:
        make_drink = True
    else:
        print("not enough milk")
        make_drink = False
    if cof == True:
        make_drink = True
    else:
        print("not enough coffee")
        make_drink = False

"===================================================="

def money_count(): #2
    global total_money
    quar = (quarters*0.25)
    dim = (dimes*0.10)
    nic = (nickles*0.05)
    pen = (pennies*0.01)

    total_money += round(quar + dim + nic + pen, 2)
    return total_money

print(water(get_ingr(choice())))









# def compare(wat, mil, cof): #3
#     if wat == True:
#         make_drink = True
#     else:
#         print("not enough water")
#         make_drink = False
#     if mil == True:
#         make_drink = True
#     else:
#         print("not enough milk")
#         make_drink = False
#     if cof == True:
#         make_drink = True
#     else:
#         print("not enough coffee")
#         make_drink = False


# compare(water(get_ingr(choice())), milk(get_ingr(choice())), coffee(get_ingr(choice())))