# def grade_statistics():
#     grades = []                         #Create list
#     grades.append(92)                   #Add value to list 
#     grades.append(51)
#     grades.append(83)
#     grades.append(37)
#     grades.append(72)
#     print('Current grades: ', grades)   #Print list 

#     total = grades[0]+grades[1]+grades[2]+grades[3]+grades[4]    #Sum values fix to total 
#     print(f'Average: {total//len(grades):.2f}')                  #Print total/len of list = average

#     grades.remove(51)                                            #Deleting by value match
#     del grades[2]                                                #Deleting by index
#     print(f'\nUpdated grades: {grades}')
#     print(f'Updated average: {sum(grades)/len(grades):.3f}')     #Printing new average with sum()
    

# grade_statistics()

# txt = 'apple'
# for var in 'python everyday':
#     print(var, end='\t')

lst = [i for i in range(10,101,10)]
for n in lst:
    print(n, end=' ')
print()

for x in range(55,4,5):
    print(x)