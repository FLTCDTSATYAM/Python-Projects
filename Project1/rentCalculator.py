### Rent Calculator ###

rent = int(input("Enter your house rent: "))
food = int(input("Enter your food expenditure of month: "))
electricity_unit = int(input("Enter no. of units: "))

charge_per_unit = int(input("Enter amount of 1unit for elctricity: "))
if(electricity_unit < 200):
    electricity_bill = 0
else:
    electricity_bill = electricity_unit * charge_per_unit

persons_per_house = int(input("Enter no. of persons in a room: "))

total_cost = rent + food + electricity_bill

total_bill = total_cost // persons_per_house

print(f"Total rent to be paid by each person in a room: {total_bill}")
