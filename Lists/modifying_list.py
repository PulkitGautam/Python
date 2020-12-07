# Modifying Lists
numbers = ['one', 'two', 'four', 'five']

# Replacing Element
numbers[2] = 'three'
print(numbers)

# Adding new Element to last
numbers.append('six')
print(numbers)

# Inserting Element in List
numbers.insert(3, 'four')
print(numbers)

# Removing Elements from List
del numbers[5]                                # Method 1 - Simple deletion of Element
print(numbers)

deleted_number = numbers.pop(4)               # Method 2 (Poping) - Deletion of Element and storing it
print(numbers)
print("The Deleted Number is " + deleted_number)

numbers.remove('four')                        # Method 3 - Deletion of element by Value (Removes only first occurence)
print(numbers)