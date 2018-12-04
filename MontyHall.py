
import random
# 1 - car
# 0 - goat

switch = 0
not_switch = 0

for i in range(10000):
    lst = [1, 0, 0]
    random.shuffle(lst)

    initial_choice = random.randrange(3)

    if lst[initial_choice] == 1:
        not_switch += 1
    else:
        switch += 1

print('switch = %d' % switch)
print('not switch = %d' % not_switch)

