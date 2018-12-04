
# [(price0, weight0), (price1, weight1), etc, (priceN, weightN)]

credit = 18
books = [(17, 5), (3, 55), (5, 12), (14, 9), (16, 1), (9, 5),
         (5, 6), (18, 13), (19, 7), (1, 20), (4, 12), (11, 1),
         (8, 6), (8, 18), (3, 4), (13, 7), (17, 22), (20, 7)]

# O(n^2) solution
idxx = []
weight = []
n = len(books)

for i in range(n-1):
    for j in range(i+1,n):
        sumPrice = books[i][0] + books[j][0]
        if sumPrice == credit:
            sumWeight = books[i][1] + books[j][1]
            idxx.append([i,j])
            # print(i,j)
            weight.append(sumWeight)

idx = weight.index(min(weight))
print(idxx[idx])
print(min(weight))


# O(n) Solution
prices = [books[i][0] for i in range(n)]
D = {}
idxx = []
weight = []
idx = 0
for price in prices:
    looking = credit - price
    if looking in D.keys():
        idxx.append([D[looking], idx])
        weight.append(books[D[looking]][1] + books[idx][1])
    D[price] = idx
    idx += 1

min_idx = weight.index(min(weight))
print(idxx[min_idx])
print(min(weight))
