

#################################### List ####################################
list = [x for x in range(1,10)]
print(list)

list.append(100)
print(list)

list.extend([1,2,3,4])
print(list)

i, x = 1, 99
list.insert(i, x) # i {0, 1, ..., len(list)}
print(list)

list.remove(x)
print(list)

list.pop() # pop last item
print(list)

x = 5
idx = list.index(x) # index of the first item whose value is x
print(idx)

count = list.count(x) # the number of times x appears in the list.
sorted_idx = [i[0] for i in sorted(enumerate(list), key=lambda x:x[1])]
sorted_list = sorted(list, reverse=True)
print('sorted list:', sorted_list, '\nsorted index:', sorted_idx)

list.reverse()
print(list)


stack = [] # first-in, last-out
stack.append(3)
stack.append(4)
stack.append(5)
s1 = stack.pop()
s2 = stack.pop()
s3 = stack.pop()
print(s1, s2, s3)


squares = [x**2 for x in range(10)]
print(squares)


grid = [(x, y) for x in [0,1,2,3,4] for y in range(5) if x!=y]
print(grid)
points = [(x, x**2) for x in range(6)]
print(points)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
nums = [num for elem in matrix for num in elem]
print(nums)
matrx_transpose = [[row[i] for row in matrix] for i in range(3)]
print('matrix transpose:', matrx_transpose)



#################################### Tuples and Sequences ####################################
tuple = 12345, 54321, 'hello!'
print(tuple[0])
print(tuple)
u = tuple, (1,2,3,4,5)
# tuple cannot be changed
x, y, z = tuple
print(x,y,z)

singleton = 'hello',
print(singleton)



#################################### Sets ####################################
# an unordered collection with no duplicate elements
set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('set:', set)

bool1 = 'orange' in set
bool2 = 'crabgrass' in set
print(bool1, bool2)

# a = set('abracadabra')
# b = set('alacazam')
# print('a:', a, 'a-b:', a-b, 'a|b:', a|b, 'a&b:', a&b, 'a^b:', a^b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)



#################################### Dictionaries ####################################
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
# keys = list(tel.keys())
# print('keys:' ,keys)
sorted_keys = sorted(tel.keys())
print('sorted keys:', sorted_keys)
bool3 = 'guido' in tel
bool4 = 'jack' not in tel
print(bool3, bool4)

dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict2 = {x: x**2 for x in (2, 4, 6)}
dict3 = dict(sape=4139, guido=4127, jack=4098)
print(dict1, '\n', dict2, '\n', dict3)



#################################### Looping Techniques ####################################
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print(key, value)

for idx, value in enumerate(['tic', 'tac', 'toe']):
    print(idx, value)

# Loop over two sequences
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = [0,4,5,2,1,1,5,-1]
for num in sorted(basket):
    print(num)


