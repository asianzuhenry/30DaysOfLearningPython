# Python Basics - Day 3

## Conditional Statements
Conditional statements allow you to execute certain blocks of code based on specific conditions. The most common conditional statements in Python are `if`, `elif`, and `else`.
```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```
In this example, the program checks if `x` is greater than 5, equal to 5, or less than 5 and prints the appropriate message. You can also use logical operators like `and`, `or`, and `not` to combine multiple conditions.
```python
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")
```
In this case, the program checks if both conditions are true before executing the print statement.


## Practice Questions
### Practice Question 1

Write a Python program that asks the user for:
- their name
- the number of items they want to buy
- the price of one item
- whether they have a discount code (`yes` or `no`)

Then:
1. Convert the number of items and price into the correct data types.
2. Calculate the total cost before discount.
3. If the user has a discount code and buys more than 3 items, apply a 15% discount.
4. If the user has a discount code but buys 3 or fewer items, apply a 5% discount.
5. If the user does not have a discount code, no discount is applied.
6. Calculate a sales tax of 8% on the final cost after discount.

7. Print a summary showing:
    - user name
    - items bought
    - original total
    - discount applied
    - tax amount
    - final amount to pay

Use variables, data type conversion, arithmetic operators, `input()` and `print()`, and conditional statements to solve the problem.

### Practice Question 2
Write a Python program to determine if a given year is a leap year. A leap year is defined as:
- It is divisible by 4;
- However, if it is divisible by 100, it must also be divisible by 400 to be a leap year.
```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

### Practice Question 3
Write a Python program to find the largest of three numbers. The program should:
1. Prompt the user to enter three numbers.
2. Use conditional statements to compare the numbers and determine which one is the largest.
```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is: {largest}")
```