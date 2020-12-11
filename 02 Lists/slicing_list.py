# Slicing a List
digit = ['one', 'two', 'three', 'four', 'five']
print(digit[1:3])


# Syntax
#        list_name(start : end+1 : skip)
#                                   omit start or end to slice list from beginning or end
#                                   negative index can be used

# Slicing can be used for copying List
list2 = digit[:]                   # This method creates two separate List
print(list2)                       # Changes don't reflect

list3 = digit                      # This method associates list to other var
print(list3)                       # Change in one reflects to another