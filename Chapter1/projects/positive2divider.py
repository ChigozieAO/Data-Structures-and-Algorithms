# P-1.30 
# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

def positive2divider(num):
    times = 0
    if num > 2:
        while num >= 2:
            num = num//2
            times += 1
        print(times)
    else:
        print('input a number greater than 2')
        

number = int(input('Type in a number:'))
positive2divider(number)
