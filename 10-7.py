#A
# for i in range(1,10,2):
#     print(i, end= ',')

# odds = list(range(1,10,2))
# print(odds)


#B
# cubes = []
# for n in range(1,11):
#     cubes.append(n*n*n)
# print(cubes)
# for v in cubes:
#     print(v)


#C
# #list of comprehension
# c = [n**3 for n in range(1,11)]
# for i in c:
#     print(i, end='|')
# print()

#2 - List indexing and slicing
evens = [n for n in range(0,101,2)]
print(evens[0], evens[-1])
# m = evens.index(54)
# n = evens.index(74)
# print(evens[:5], evens[-5:], evens[m:n+1], sep = '\n')
print(evens[:5], evens[-5:], evens[evens.index(44):evens.index(88)+1], sep = '\n')


#3
n_one = [x*4 for x in range(11)]
print(n_one)
n_two = []
