# Sorting List Alphabetically
country = ['USA', 'Australia', 'Belgium', 'India', 'Canada', 'Brazil', 'Mexico']

country.sort()
print(country)

country.sort(reverse=True)             # Sorting in Reverse Alphabetical Order
print(country)

# Sorting List Temporarily
country = ['USA', 'Australia', 'Belgium', 'India', 'Canada', 'Brazil', 'Mexico']
ar = sorted(country)
print(ar)
print(country)                         # List Remains Same