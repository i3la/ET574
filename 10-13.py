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

#age = int(input('Please enter your age: ')) #simpler way
#if age < 0 :
#    print('Invalid age.')
#elif age < 2 :
#    print("You're a baby.")
#elif age < 4  :
#    print("You're a toddler.")
#elif age < 13  :
#    print("You're a kid.")
#elif age < 20  :
#    print("You're a teenager.")
#elif age < 65  :
#    print("You're an adult.")
#else:
#    print("You're an elder.")


#2
#usernames = ['Tom','Jerry','Bob','Dora','ADMIN']
#if usernames:
#    for username in usernames:
#        if username == 'ADMIN':
#            print("Hello ADMIN, would you like to see a status report?")
#        else:
#            print(f"Hello {username}, thank you for logging in again!")
#else:
#    print("We need to find some users")


#usernames = []
#if usernames:
#    for username in usernames:
#        if username == 'ADMIN':
#            print("Hello ADMIN, would you like to see a status report?")
#        else:
#            print(f"Hello {username}, thank you for logging in again!")
#else:
#    print("We need to find some users")


#3
#current_users = ['admin', 'tom', 'jerry', 'Dora', 'GEORGE']
#username = input("Enter your user name: ")
#lowercase_users = [user.lower() for user in current_users]
#if username.lower() in lowercase_users:
#    print(f"Sorry {username}, that name is taken.\nCurrent users: {current_users}")
#else:
#    current_users.append(username)
#    print(f"Great {username}, is still available.\nUpdated user list: {current_users}")

vehicles = ['car', 'Truck', 'boat', 'PLANE']
print(f"vehicles = {vehicles}")
letter = input("Enter a search letter: ")
if len(letter) > 1:
    print("Invalid search letter.")
else:
    letter = letter.lower()
    for position in range(len(vehicles)):
        vehicle = vehicles[position]
        if letter in vehicle.lower():
            print(f"{vehicle} contains '{letter}' and it is in position {position}.")
        else:
            print(f"{vehicle} does not contain '{letter}'.")