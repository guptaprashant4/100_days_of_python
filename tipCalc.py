print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
num_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))

bill_w_tip = total_bill * (tip_percentage/100) + total_bill
amnt_per_person = bill_w_tip / num_people

print("Each person should pay: " + amnt_per_person)