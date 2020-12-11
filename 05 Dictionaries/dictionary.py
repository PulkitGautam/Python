# Dictionary is a collection of key-value pairs.
detail = {'Name': "Pulkit Gautam", 'City': "Saharanpur", 'Age': 18}
print(detail['Name'])
print(detail['City'])
print(detail['Age'])

# Adding new Key-Value Pair
detail['Colour'] = "Blue"
print(detail)

# Modifying Dictionary
detail['Colour'] = "Black"
print(detail)

# Deleting Key-Value Pair
del detail['Age']
print(detail)