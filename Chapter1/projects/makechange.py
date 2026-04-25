# P-1.31
# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

charged = float(input("Amount charged: "))
given = float(input("Amount given: "))

change = given - charged

if change < 0:
    print("Not enough money given.")
else:
    change = round(change * 100)

    denominations = [
        (10000, "$100"),
        (5000, "$50"),
        (2000, "$20"),
        (1000, "$10"),
        (500, "$5"),
        (100, "$1"),
        (25, "25¢"),
        (10, "10¢"),
        (5, "5¢"),
        (1, "1¢")
    ]

    print("Change to give:")

    for value, name in denominations:
        count = change // value
        if count > 0:
            print(f"{name}: {count}")
        change %= value