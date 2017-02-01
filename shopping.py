shopping_list = ["apples", "oranges", "bananas"]

def items_in_my_cart(my_shopping_list):
    your_items = raw_input("What would you like to add to the cart? ").lower()
    if your_items in my_shopping_list:
        print "We already have that. Add something else!"
    else:
        my_shopping_list.append(your_items)
    return my_shopping_list

shopping_list = items_in_my_cart(shopping_list)
shopping_list.sort()
print shopping_list
