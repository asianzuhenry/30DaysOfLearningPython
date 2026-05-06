# Lists
my_list = [1, 2, 3, 'hello', True]
print(my_list)  # Output: [1, 2, 3, 'hello', True]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'hello'


# Modifying elements
my_list[1] = 42
my_list[4] = False
print(my_list)  # Output: [1, 42, 3, 'hello', False]

# List methods
my_list.append('world')
print(my_list)  # Output: [1, 42, 3, 'hello', False, 'world']

my_list.remove(3)
print(my_list)  # Output: [1, 42, 'hello', False, 'world']

my_list.insert(2, 'new')
print(my_list)  # Output: [1, 42, 'new', 'hello', False, 'world']



