#  Practice Question 1

# This program calculates the total cost of items purchased, 
# applies discounts based on the number of items and whether the user has a discount, 
# and then calculates the final amount after applying sales tax.
name = input("Please enter your name: ")
number_of_items = int(input("Enter number of items: "))
cost_per_item = int(input("Enter cost of each item: "))
has_discount = input("Do you have a discount(yes/no): ")

total_cost = number_of_items * cost_per_item

# Applying discounts based on the number of items and whether the user has a discount
if has_discount == "yes" and number_of_items > 3:
    discount = (total_cost * 15) / 100 # 15% discount for more than 3 items
elif has_discount == "yes" and number_of_items <= 3:
    discount = (total_cost * 5) /  100 # 5% discount for 3 or fewer items
elif has_discount == "no":
    discount = 0 # no discount if the user doesn't have a discount

cost_after_discount = total_cost - discount
sales_tax = (cost_after_discount * 8) / 100 # calculating sales tax
final_amount = cost_after_discount - sales_tax

# Displaying the summary of the purchase
print("===SUMMARY===")
print(f"Name: {name}")
print(f"Number of items: {number_of_items}")
print(f"Original total: {total_cost}")
print(f"Discount applied: {discount}")
print(f"Tax amount: {sales_tax}")
print(f"Final amount to pay: {final_amount}")