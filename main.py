# Base Challenge and Extra #1 and 3:
# -----------------------------------------


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
count = 0

user_num = int(input('Enter a number:\n'))

while count < len(a):
    if a[count] < user_num:
        b.append(a[count])
    count += 1

print('List a = {}'.format(a))
print('Items from list a that are smaller than {} are {}'.format(user_num, b))
# -----------------------------------------



'''
# Solution I found online:
# 
# user_num = int(input('Enter a number:\n'))
# print([b for b in a if b < user_num])
# 
#
'''