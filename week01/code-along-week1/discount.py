
# Author:       Bright Kwaku Boateng
# Purpose:      Code Along Activity(week 01)
# Description:  User gets a discount of 10% when they order items worth $50.00
#               and above...!


import datetime

quantity = 1
price = 0
subtotal = 0

while quantity != 0:
    quantity = float(input("What is the quantity of all your purchases: "))
    
    if quantity != 0:
        price = float(input("What is the price: "))

    subtotal += quantity * price

    print(f"Subtotal is = {subtotal:.2f}")

discount_rate = 0.1
tax_rate = 0.06

today = datetime.datetime.now()
day = today.weekday()

discount_amount = subtotal * discount_rate
tax_amount = subtotal * tax_rate

if subtotal >= 50 and (day == 1 or day == 2):
    amount_due = subtotal - discount_amount + tax_amount
else:

    buy_more = 50 - subtotal

    discount_amount = 0.00
    amount_due = subtotal + tax_amount

    print(f"You need to spend {buy_more:.2f} in other to get 10% discount...")

    print(f"""Total order: {subtotal:.2f},
    Discount = {discount_amount:.2f},
    Sales Tax amount: {tax_amount:.2f},
    TOTAL Due: {amount_due:.2f}

    """)