# #1 For: 
# for x in range(1,101):
#        if x % 2 == 0:
#               print(x, end = ' ')
# print()
#
# #1 While:
# x = 1
# while x < 101:
#     if x % 2 == 0:
#         print (x, end=' ')
#     x += 1




# #4 for:
# for i in range(9,0,-1):
#     print(i)
# else:
#     print('Happy New Year!')
#
# #4 while:
# i = 9
# while i > 0:
#     print(i)
#     i -= 1
# print('Happy New Year!')




#8 (missing functions)
# n = []
# x = 1
# try:
#     while x != 0:
#         x = eval(input('Enter a number or 0 to stop: '))
#         if x != 0:
#             n.append(x)
#     else:
#         print(f'Sum = {sum(n):.3f}\nAverage = {sum(n)/len(n):.2f}\nNumber(s) entered =\n{n}')

# except:
#     print('Invalid input')




#7
try:
    n1 = int(input('Enter an integer number n1: '))
    n2 = int(input('Enter an integer number n2: '))
    if n1 < n2:
        i = n1
        while i <= n2:
            print(i, end='|')
        i+=1
    elif n1 > n2:
        for i in range(n1,n2-1,-1):
            print(i, end='|')
    else:
        print('n1 = n2')

except:
    print('Invalid input')
