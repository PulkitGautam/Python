# Using for Loop through Dictionary
Employee = {
    'Name': "Ravi Kumar",
    'Employee No': 25,
    'Department': "Financial"
}

for key, value in Employee.items():
    print(f"{key} of employee is {value} \n")

# Syntax
#                 for key_var, value_var in dict-name.items():
#                    /...  Body .../
         
# If only one variable is given it is taken for key
# Similarly list methods keys, value can be used