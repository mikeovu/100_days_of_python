'''
We're going to build a tip calculator.

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:

(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60

Demo: https://appbrewery.github.io/python-day2-demo/
'''

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100 # converts tip percentage into decimal for calculation. Example, for a ten percent tip 10 / 100 = .10
total_tip_bill = bill * tip_percent # Calculates how much the tip would be. If the bill was $100, it would be $100 * .10 = $10
total_bill = bill + total_tip_bill # Adds the bill to the tip dollar amount for the total bill amount. This would be $100 + $10 = $110
bill_per_person = total_bill / people # Divides the total bill amount by the amount of people, if there were 2 people, it would be 110 / 2 = $55
final_amount = round(bill_per_person, 2) 
# Use the round function to round the amount each person 
# should pay to 2 decimal places for better readability and to match currency format.

print(f"Each person should pay: :${final_amount} ")

