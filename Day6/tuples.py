# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 4

# Modifying elements (This will raise an error because tuples are immutable)
# my_tuple[1] = 42  # Uncommenting this line will raise a TypeError
# Tuple methods
# Tuples have fewer methods than lists because they are immutable
print(my_tuple.count(2))  # Output: 1
print(my_tuple.index(3))  # Output: 2

# Tuples can be used to store heterogeneous data
mixed_tuple = (1, 'hello', True, 3.14)
print(mixed_tuple)  # Output: (1, 'hello', True, 3.14)