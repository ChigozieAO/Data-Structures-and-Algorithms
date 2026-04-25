# P-1.29
# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.

string_list = ['a', 'c', 't', 'd', 'o', 'g']
def word_form(listed, current=''):

    if not listed:
       print(current)
       return

    for i in range(len(listed)):
        remaining = listed[:i] + listed[i+1:]
        word_form(remaining, current + listed[i])

        
word_form(string_list)