# this is ok tested.
search_desc = 'This is a best Usha fan.'
search_category = 'Electronics or Electrical'
search_name = 'Motor'
print(search_name)
print(search_category)
print(search_desc)
user_input = input("Enter the string that you want to search:")
print()


# user_input_list = user_input.split()
# print(user_input_list)


def search(user_choice, *desc):
    # a = desc
    # print(a)
    user_input_list = user_choice.lower().split()
    # print(user_input_list)
    # print('This is entered by user:', user_input_list)
    # for i in user_input_list:
    #     if i in desc:
    #         return True
    # else:
    #     return False
    for item in desc:
        # item = item.lower()
        for i in user_input_list:
            if i in item.lower():
                print('this item in the list')
                print(item)
                return
    else:
        print('This is not in the list.')
        return


search(user_input, search_desc, search_name, search_category)
