my_name = input("What is your first name ?: \n")
partner_name = input("What is your spouse's first name ?:\n")
print(f"\nHello {my_name} nice to meet you. Welcome to your monthly income & expense calculator !\nLets start:\n ")
rent = float(input("Enter your monthly RENT Payment for your Vienna Apartment: \n$"))
Car = float(input("Enter your Honda CRV monthly Car Payment: \n$"))
internet = float(input("Enter your monthly Internet Bill Payment: 0 or more numerical value \n$"))
electricity = float(input("Enter your monthly Electricity Bill Payment: 0 or more numerical value \n$"))
hoa = float(input("Do you pay any HOA payment, i guess not: 0 or more numerical value \n$"))
water = float(input("Enter your monthly WATER Bill Payment: 0 or more numerical value \n$"))
health_ins = float(input(f"Enter your monthly Health Insurance Payment for you & {partner_name}: \n$"))
car_ins = float(input("Enter your monthly Car Insurance Payment: \n$"))
car_fuel = int(input("Enter your monthly approx. Car Fuel Expenses: \n$"))
restaurant = int(input("Around how much you spend monthly on your Restaurent Food ?: 0 or more numerical value \n$"))
misc = input("Do you have any other expenses ? enter y for Yes or N for no: \n")

total_expense = rent + Car + internet + electricity + hoa + water + health_ins + car_ins + car_fuel + restaurant
print("\n")
print(f"{my_name} Thank you for that info, lets look at your income scenario:\n")
income = float(input("How much approx. you bring home on each paycheck bi-weekly ? \n$"))
income1 = float(input(f"How much approx. {partner_name} brings home on each paycheck bi-weekly ? \n$"))
monthly_income = (income + income1) * 2
monthly_saving = monthly_income - total_expense

print(f"\n{my_name}, Your monthly expense is ${total_expense}.\nYour monthly take home income is ${monthly_income}.\nYou can save monthly upto ${monthly_saving} if you try to be more mindful about your spendings.")

