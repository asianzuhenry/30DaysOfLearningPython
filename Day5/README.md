# Day 5: Functions and Variable Scope

## What is a Function?
A function is a block of code that performs a specific task. It can take inputs, process them, and return an output. Functions help to break down complex problems into smaller, manageable pieces and promote code reusability.

## Defining a Function
You can define a function using the `def` keyword followed by the function name and parentheses.
### Syntax
```python
def function_name(parameters):
    # code block
```
### Example
```python
def greet(name):
    return f"Hello, {name}!"    

print(greet("Alice"))
```
## Function Parameters and Arguments
- **Parameters** are the variables listed inside the parentheses in the function definition. They act as placeholders for the values that will be passed to the function.
- **Arguments** are the actual values passed to the function when it is called.
### Example
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```
## Return Statement
The `return` statement is used to exit a function and return a value to the caller.
### Example
```python
def square(x):
    return x * x
print(square(4))  # Output: 16
```
## Default Parameters
You can assign default values to parameters in a function. If the caller does not provide a value for that parameter, the default value will be used.
### Example
```python
def greet(name="World"):
    return f"Hello, {name}!"
print(greet())  # Output: Hello, World!
print(greet("Alice"))  # Output: Hello, Alice!
```

## Variable Scope
The scope of a variable is the region of the code where it is defined and can be accessed. Variables defined inside a function are called local variables and can only be accessed within that function. Variables defined outside of any function are called global variables and can be accessed throughout the code.
### Example
```python
def my_function():
    local_var = "I am a local variable"
    print(local_var)
```
```python
my_function()  # Output: I am a local variable
print(local_var)  # This will raise an error because local_var is not defined outside the function
```