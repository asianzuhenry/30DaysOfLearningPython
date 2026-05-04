# DAY 4: LOOPS
## For Loop
The `for` loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.

### Syntax
```python
for variable in iterable:
    # code block
```

### Example
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

## While Loop
The `while` loop is used to execute a block of code as long as a specified condition is true.

### Syntax
```python
while condition:
    # code block
```

### Example
```python
i = 1
while i < 6:
    print(i)
    i += 1
```

## Nested Loops
You can use one loop inside another loop. This is called a nested loop.
### Example
```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
```

## Loop Control Statements
- `break`: Exits the loop when a specified condition is met.
- `continue`: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
- `pass`: Does nothing, acts as a placeholder.

### Example
```python
for x in range(10):
    if x == 5:
        break
    print(x)
```

## Practice Exercise
1. Write a `for` loop that prints the numbers from 0 to 9.
2. Write a `while` loop that prints the numbers from 1 to 5.
3. Write a nested loop that prints all combinations of two lists: `colors = ["red", "green", "blue"]` and `shapes = ["circle", "square", "triangle"]`.
4. Write a `for` loop that prints all the characters in the string "Hello, World!".
5. Write a program that asks the user to enter a number, then use a `for` loop to print the multiplication table for that number (up to 10).
