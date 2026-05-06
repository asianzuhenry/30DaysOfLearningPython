# Day 6: Lists and Tuples

## Lists
A list is a collection which is ordered and changeable. In Python, lists are written with square brackets `[]`.
```python
my_list = [1, 2, 3, 'hello', True]
print(my_list)  # Output: [1, 2, 3, 'hello', True]
```
You can access list items by their index:
```python
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'hello'
```
Lists are mutable, which means you can change their content:
```python
my_list[1] = 'world'
print(my_list)  # Output: [1, 'world', 3, 'hello', True]
```
You can also add items to a list using the `append()` method:
```python
my_list.append(4)
print(my_list)  # Output: [1, 'world', 3, 'hello', True, 4]
```

## Tuples
A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets `()`.
```python
my_tuple = (1, 2, 3, 'hello', True)
print(my_tuple)  # Output: (1, 2, 3, 'hello', True)
```
You can access tuple items by their index:
```python
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'hello'
```
Tuples are immutable, which means you cannot change their content after they are created:
```python
my_tuple[1] = 'world'  # This will raise a TypeError
```
However, you can concatenate tuples to create a new tuple:
```python
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 'hello', True, 4, 5)
```
In summary, lists are mutable and can be modified after creation, while tuples are immutable and cannot be changed once they are created. Both lists and tuples can store a variety of data types and are ordered collections.