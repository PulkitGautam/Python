# Uing if Statement for Checking for Conditions
x = 10
y = 15

if x > y :
    print ('x is Greater.')
elif y > x :
    print ('y is Greater.')
else:
    print ('x equals y.')

# Checking occurence in a List
colors = ['black', 'yellow', 'green', 'orange']

if 'red' in colors:                         # in Keyword
    print('Red Present')

if 'blue' not in colors:
    print('Blue Absent')                  # not in Keyword