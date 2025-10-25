# List Creation
my_list = [1, 2, 3, 4, 5]
empty_list = []
list_from_range = list(range(10))

# List Adding/Appending
my_list.append(6)  # Adds 6 to the end
my_list.extend([7, 8, 9])  # Extends with another list
my_list.insert(0, 0)  # Inserts 0 at index 0

# List Slicing
first_three = my_list[:3]  # [0, 1, 2]
last_three = my_list[-3:]  # [7, 8, 9]
middle = my_list[2:5]  # [2, 3, 4]
every_other = my_list[::2]  # [0, 2, 4, 6, 8]
reversed_list = my_list[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# List Comprehension
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
nested_comprehension = [[i*j for j in range(3)] for i in range(3)]  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# List Removing
my_list.remove(5)  # Removes first occurrence of 5
popped = my_list.pop()  # Removes and returns last element
popped_index = my_list.pop(2)  # Removes and returns element at index 2
del my_list[1:3]  # Deletes slice

# List Searching and Counting
index_of_4 = my_list.index(4)  # Returns index of first 4
count_of_2 = my_list.count(2)  # Counts occurrences of 2

# List Sorting and Reversing
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(unsorted)  # [1, 1, 2, 3, 4, 5, 6, 9]
unsorted.sort()  # Sorts in place
unsorted.reverse()  # Reverses in place

# List Copying
shallow_copy = my_list.copy()
deep_copy_example = [my_list[:]]  # Shallow copy using slice

# List Membership
is_5_in_list = 5 in my_list
is_10_not_in_list = 10 not in my_list

# List Length and Clearing
length = len(my_list)
my_list.clear()  # Empties the list

# Advanced List Operations
zipped = list(zip([1, 2, 3], ['a', 'b', 'c']))  # [(1, 'a'), (2, 'b'), (3, 'c')]
enumerated = list(enumerate(['a', 'b', 'c']))  # [(0, 'a'), (1, 'b'), (2, 'c')]
filtered = list(filter(lambda x: x > 5, [3, 7, 1, 9, 4, 6]))  # [7, 9, 6]
mapped = list(map(lambda x: x*2, [1, 2, 3, 4]))  # [2, 4, 6, 8]

# List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2  # [1, 2, 3, 4, 5, 6]

# List Repetition
repeated = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# Nested Lists
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5, 6]
print(len(nested))
