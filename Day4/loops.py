# LOOPS
# for, while, nested

# for
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# while
n = 1
while n < 10:
    print(f"Number {n}")
    n += 1

# nested loops
fruits = ["apples", "oranges", "pineapples"]
colors = ["red", "yellow", "green"]

for fruit in fruits:
    for color in colors:
        print(fruit, color)