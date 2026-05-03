'''
Jake
IS 303 - A01

Tip Splitter
This program splits a restaurant bill among friends, including a tip,
and shows the per-person amount.

Inputs:
- Restaurant name (string)
- Bill amount (float)
- Tip percentage (float)
- Number of people (int)

Processes:
- Convert bill, tip percentage, and number of people to numbers
- Calculate tip amount: bill * (tip% / 100)
- Calculate total with tip: bill + tip amount
- Calculate per-person amount: total / number of people

Outputs:
- Print the restaurant name, bill, tip, total, and per-person share
'''

restaurant_name = input("What is the restaurant name? ")
bill_amount = float(input("What is the bill amount? "))
tip_percent = float(input("What tip percentage? "))
num_people = int(input("How many people are splitting? "))

tip_amount = bill_amount * (tip_percent / 100)
total_with_tip = bill_amount + tip_amount
per_person = total_with_tip / num_people

print("---")
print(f"{restaurant_name} | ${bill_amount:.2f} bill | {tip_percent}% tip | {num_people} people")
print(f"Tip: ${tip_amount:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")
print(f"Each person pays: ${per_person:.2f}")

