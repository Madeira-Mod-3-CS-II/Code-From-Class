phrase = "Robots are the best!"

# Print the first character of the phrase
print(phrase[0])
print(phrase[-len(phrase)])

# Print the length of phrase (number of chars in phrase)
print(len(phrase))

# If we try to print what is at index 20. There isn't actually a character
# at index 20. IndexError: string index out of range.
# print(phrase[20])

# Print the last character of a string
print(phrase[len(phrase)-1])
print(phrase[-1])

# Special Characters
# Escape Characters
# \t - tab
# \n - newline
# \\ - backslash
# \" - quote
# \' - apostrophe

wish = " My first class starts at: \t 11am"
lunch_main = "Steak"
lunch_side = "Fries"
lunch_drink = "Water"
lunch_dessert = "Cake"
lunch_after = "Ice Cream"

print(lunch_main, end="\t")
print(lunch_side, end="\t")
print(lunch_drink, end=",\t")
print(lunch_dessert, end=" $4.75\n")
print(lunch_after)
print(wish)

# Fstrings
# Fstrings allow us to fill-in-the-blank in a nice way

lunch_order = f"My lunch order is: {lunch_main} \t {lunch_side} \t {lunch_drink} \t"
dessert_order = f"For Dessert: {lunch_dessert} \t Cost: ${4.756:.2f}"

print(lunch_order)
print(dessert_order)

# String Methods
print(wish.strip())     # strip() gets rid of white space at the beginning and end
                        # of a string

wish_list = wish.split()    # Split creates a list from wish by splitting
print(wish_list)            # on spaces by default

# Comma Seperated Values (csv)
lunch = "sandwich, chips, cauliflower, soda"
lunch_list = lunch.split(",")
print(lunch_list)

def strip_list(list_items):
    '''
    Purpose: To strip any whitespace at the beginning and end of each
    item in list_items

    Parameters: list_items - the list of items to be stripped of white space; list str

    Return Value; list_items with the white space removed; list str
    '''

    for index in range(len(list_items)):
        list_items[index] = list_items[index].strip()

    return list_items

print(strip_list(lunch_list))
