print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
)

# declare initial menu

menu = {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0, 'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0,
        'A Literal Garden': 0, 'Ice Cream': 0, 'Cake': 0, 'Pie': 0, 'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}

print("What would you like to order?")

# Put order


def handle_order():
    order = 0
    while (order != "quit"):
        order = input()
        if (order == "quit"):
            break
        for item in menu:
            if order == item:
               
                print(
                    f"  order of {item} have been added to your meal")
                break
        else:
            print("This order is not available")


handle_order()
