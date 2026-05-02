# Day Two

## Contents
- Data Types
- Type Conversion
- String Methods
- Basic Operations
- Input and Output

## Data Types
In Python, data types are used to classify the type of data that a variable can hold. Each data type has its own characteristics and operations that can be performed on it. Understanding data types is crucial for writing efficient and effective code.

### Examples of data types in Python include:
- **Integer**: Whole numbers, e.g., `42`, `-7`
- **Float**: Decimal numbers, e.g., `3.14`, `-0.001`
- **String**: Text enclosed in quotes, e.g., `"Hello, World!"`, `'Python'`
- **Boolean**: Represents `True` or `False`
```python
is_raining = True
is_sunny = False
```
- **List**: Ordered collection of items, e.g., `[1, 2, 3]`, `['apple', 'banana', 'cherry']`
- **Tuple**: Ordered, immutable collection of items, e.g., `(1, 2, 3)`, `('apple', 'banana', 'cherry')`
- **Dictionary**: Collection of key-value pairs, e.g., `{'name': 'Alice', 'age': 30}`

## Type Conversion
Type conversion, also known as type casting, is the process of converting a variable from one data type to another. This can be done explicitly using built-in functions or implicitly by Python when necessary.
### Examples of type conversion:
```python
# Explicit type conversion
num_str = "123"
num_int = int(num_str)  # Converts string to integer
print(num_int)  # Output: 123
# Implicit type conversion
result = 5 + 3.2  # Integer is implicitly converted to float
print(result)  # Output: 8.2
```
Understanding data types and type conversion is essential for writing robust and error-free code in Python. It allows you to manipulate data effectively and ensures that your program behaves as expected. 

## String Methods
Python provides a variety of built-in string methods that allow you to manipulate and work with strings efficiently. Some common string methods include:
- `lower()`: Converts all characters in a string to lowercase
- `upper()`: Converts all characters in a string to uppercase
- `strip()`: Removes leading and trailing whitespace from a string
- `split()`: Splits a string into a list of substrings based on a specified delimiter
- `replace()`: Replaces occurrences of a specified substring with another substring
### Example of string methods:
```python
text = "  Hello, World!  "
print(text.lower())  # Output: "  hello, world!  "
print(text.upper())  # Output: "  HELLO, WORLD!  "
print(text.strip())  # Output: "Hello, World!"
print(text.split(", "))  # Output: ['  Hello', 'World!  ']
print(text.replace("World", "Python"))  # Output: "  Hello, Python!  "
```
Using string methods can help you manipulate and format strings in various ways, making it easier to work with text data in your programs.

## Basic Operations
Python supports a variety of basic operations that can be performed on different data types. These operations include arithmetic operations, comparison operations, and logical operations.
### Examples of basic operations:
```python
# Arithmetic operations
a = 10
b = 5
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50
print(a / b)  # Output: 2.0
print(a % b)  # Output: 0   // Modulo operation -> returns the remainder of the division
# Comparison operations
print(a > b)  # Output: True
print(a < b)  # Output: False
print(a == b)  # Output: False
print(a != b)  # Output: True
# Logical operations
is_sunny = True
is_warm = False
print(is_sunny and is_warm)  # Output: False
print(is_sunny or is_warm)   # Output: True
print(not is_sunny)          # Output: False
```
Understanding these basic operations is essential for performing calculations, making decisions, and controlling the flow of your program. They form the foundation of programming and are used in almost every aspect of coding.

## Input and Output
In Python, you can use the `input()` function to get user input and the `print()` function to display output to the console.
### Example of input and output:
```python
# Getting user input
name = input("Enter your name: ")
age = input("Enter your age: ")
# Displaying output
print("Hello, " + name + "! You are " + age + " years old.")
```
In this example, the `input()` function prompts the user to enter their name and age, and the `print()` function displays a greeting message that includes the user's input. This allows you to interact with the user and create dynamic programs that can respond to user input.

Understanding how to use input and output is crucial for creating interactive programs that can take user input and provide feedback or results based on that input. It allows you to create more engaging and personalized applications.

