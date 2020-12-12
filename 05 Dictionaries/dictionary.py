# Dictionary is a collection of key-value pairs.
detail = {'Name': "Pulkit Gautam", 'City': "Saharanpur", 'Age': 18}
print(detail['Name'])
print(detail['City'])
print(detail['Age'])

# Lists and Dictionary in a Dictionary
Profile : {
    'Name' : {
        'Fist_Name': "Pulkit",
        'Last_Name': "Gautam"
    },
    'Languages': ["Python", "C++", "JavaScript"]
}

# Adding new Key-Value Pair
detail['Colour'] = "Blue"
print(detail)

# Modifying Dictionary
detail['Colour'] = "Black"
print(detail)

# Deleting Key-Value Pair
del detail['Age']
print(detail)