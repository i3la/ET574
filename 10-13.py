#3
# n_one = [x*4 for x in range(11)]
# print(n_one)

# n_two = []
# for n in list(n_one):
#     n_two.append(n//2)
# print(n_two)

# n_three = n_two[:]
# for i in range(11):
#     n_three[i]= n_two[i]//2
# print(n_three)


#4 
# try:
#     r = int(input('Enter a range: '))
#     i = int(input('Enter an integer number: '))

#     print(f"Multiplication Table of {r}")
#     for n in range(1,r+1):
#         print(f"{n}\t*\t{i}\t=\t{n*i}")
# except:
#     print('Invalid input')



#1 Decision Structure

# age = int(input('Please enter your age: '))  Redundant way :(((
# if age < 0 :
#     print('Invalid age.')
# elif age < 2 :
#     print("You're a baby.")
# elif (age == 2) or (age < 4)  :
#     print("You're a toddler.")
# elif (age == 4) or (age < 13)  :
#     print("You're a kid.")
# elif (age == 13) or (age < 20)  :
#     print("You're a teenager.")
# elif (age == 20) or (age < 65)  :
#     print("You're an adult.")
# else:
#     print("You're an elder.")


age = int(input('Please enter your age: ')) #simpler way
if age < 0 :
    print('Invalid age.')
elif age < 2 :
    print("You're a baby.")
elif age < 4  :
    print("You're a toddler.")
elif age < 13  :
    print("You're a kid.")
elif age < 20  :
    print("You're a teenager.")
elif age < 65  :
    print("You're an adult.")
else:
    print("You're an elder.")