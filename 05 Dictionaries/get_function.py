# get() function prevents Error if required key-value is not present
book = {
    'Name': "A Brief History of Time",
    'Author': "Stephen Hawkings"
    }

book.get('Name', "No Book Available")               # Prints Name of Book
book.get('Publisher', "No Information")             # Print no information message

# Syntax
#         dict_name.get(key_name, optional_message)
#                                                      if second arugment is absent, None is returned