import string

print(string.punctuation)
# print(string.whitespace)
# Que:Write a function to remove the punctuation from  the given string.
user_string = 'Hello How *@Q)( you.'


def remove_punc(user_text):
    punc = string.punctuation
    analyzed_text = ''
    for text in user_text:
        if text not in punc:
            analyzed_text += text
    return analyzed_text


# calling the function
print(user_string)
print('Analyze string is:', remove_punc(user_string))
 
 print("Hello World!")