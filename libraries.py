
# import numpy as np
# from sklearn import tree
# from queue import PriorityQueue

import re
string = 'tea for too'
new_string = string.replace('too', 'two')
print(new_string)


import math
print (math.exp(1))
pi = [str(round(math.pi, i)) for i in range(10)]
print('pi: ', pi)

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, -float('inf'), 47.8, float('inf')]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):       # math.isinf(value)
        filtered_data.append(value)
print(sorted(filtered_data))


import random
fruit = random.choice(['apple', 'pear', 'banana'])
print(fruit)
samples = random.sample(range(100), 10) # sampling without replacement
print(samples)
print(random.random()) # random float (0,1)
print(random.randrange(1,10)) # random int {1,..., 9}
lst = [x for x in range(1,10)]
random.shuffle(lst)
print(lst)


import statistics
data = [1,2,3,4,6.5,1,-1.3]
mean = statistics.mean(data)
median = statistics.median(data)
var = statistics.variance(data)
print('mean: %.2f, median %.2f, var: %.2f' % (mean, median, var))











