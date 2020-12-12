# Methods used to create List
Address = {
    'Landmark': "Taj Mahal",
    'City': "Agra",
    'Country': "India"
}

print(Address.items())
print(Address.keys())
print(Address.values())

# set() can be used for avoiding repeated values
subject = {
    'Student1': "Maths",
    'Student2': "Physics",
    'Student3': "Maths",
    'Student4': "Chemistry",
    'Student5': "Physics"
}

print(subject.values())
print(set(subject.values()))