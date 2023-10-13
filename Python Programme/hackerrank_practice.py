n = int(input("How many commands you want to perform:"))
lst = []

arr = []


def check_input(text):
    """
    This function is used to check user choice.
    :param text:
    :return:bool
    """
    if text in arr:
        return True


'''
arr = ['append', 'insert', 'remove', 'sort', 'reverse', 'pop', 'print']
for i in range(n):
    if check_input(user_choice):
        if user_choice in ['append', 'insert', 'remove']:
            user_value = input(f"enter the value that you want to {user_choice}:")
            if user_choice == 'append':
                lst.append(user_value)
            elif user_choice == 'insert':
                index = int(input("which position you want to insert the value:"))
                lst.insert(index, user_value)
            elif user_choice == 'remove':
                if len(lst) != 0:
                    user_value = input("enter the value that you want to remove:")
                    lst.remove(user_value)
                else:
                    print('List has no element.')
        else:
            if user_choice == 'sort':
                lst.sort()
            elif user_choice == 'reverse':
                lst.reverse()
            elif user_choice == 'pop':
                # if list is not empty.
                if len(lst) != 0:
                    lst.pop()
                else:
                    print('List is no element.')
            elif user_choice == 'print':
                print(lst)
    # if user_choice is invalid then terminate the loop.
    else:
        print("Please enter a valid operation.")
        break
'''


# Ye fix karna hai. the light went out.
def lst_operation():
    user_choice = input('enter command and space separated value:').split()
    # then store user choice as a user_input
    user_input = user_choice[0]
    if user_input in ['insert', 'append', 'remove']:
        if user_input == 'insert':
            index = int(user_choice[1])
            value = int(user_choice[2])
            lst.insert(index, value)
            return lst
        else:
            if user_input == 'append':
                value = int(user_choice[1])
                lst.append(value)
                return lst
            elif user_input == 'remove':
                if len(lst) != 0:
                    value = int(user_choice[1])
                    lst.remove(value)
                    return lst
                else:
                    print("List has no element.")

    else:
        if user_input == 'sort':
            lst.sort()
            return lst
        elif user_input == 'reverse':
            lst.reverse()
            return lst
        elif user_input == 'pop':
            # if list is not empty.Then remove last element into the list.
            if len(lst) != 0:
                lst.pop()
                return lst
            else:
                print('List is no element.')
        elif user_input == 'print':
            print(lst)


for i in range(n):
    lst_operation()

