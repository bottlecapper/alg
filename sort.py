from queue import PriorityQueue

class Solution():
    """
    sort
    """
    def insertionSort(self, list):
        """
        :param list: List[int]
        :return: List[int]
        """
        for i in range(1, len(list)):

            candidate = list[i]
            position = i

            while candidate < list[position - 1] and  position > 0:
                list[position] = list[position - 1]
                position -= 1

            list[position] = candidate

        return list


    def mergeSort(self, list):
        """
        :param list: List[int]
        :return: List[int]
        """
        if len(list) == 1:
            return list

        mid = len(list) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        lefthalf = self.mergeSort(lefthalf)
        righthalf = self.mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i += 1
            else:
                list[k] = righthalf[i]
                j += 1
            k += 1

        if i < len(lefthalf):
            list[k:] = lefthalf[i:]
        else:
            list[k:] = righthalf[j:]

        return list


    def quickSort(self, list):
        self.subQuickSort(list, 0, len(list)-1)
        return list

    def subQuickSort(self, list, start, end):
        if start < end:
            split = self.partition(list, start, end)
            self.subQuickSort(list, start, split-1)
            self.subQuickSort(list, split+1, end)

    def partition(self, list, start, end):
        pivotvalue = list[start]
        leftmark = start + 1
        rightmark = end
        done = False
        while not done:
            while leftmark <= rightmark and list[leftmark] <= pivotvalue:
                leftmark += 1
            while leftmark <= rightmark and list[rightmark] >= pivotvalue:
                rightmark -= 1
            if leftmark > rightmark:
                done = True
            else:
                list[leftmark], list[rightmark] = list[rightmark], list[leftmark]

        list[start], list[rightmark] = list[rightmark], list[start]
        return rightmark


    def countingSort(self, list, maxValue):
        # O(n), assume max(list) < maxValue, and type(list) = List[int]
        count = [0]*maxValue
        for num in list:
            count[num] += 1
        res = []
        for i in range(maxValue):
            while count[i] > 0:
                res.append(i)
                count[i] -= 1

        return res


    def heapSort(self, list):
        # O(nlgn)
        res = []
        pq = PriorityQueue()
        for num in list:
            pq.put(num)
        while not pq.empty():
            res.append(pq.get())

        return res



### TEST ###

opt = Solution()
list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

sorted_list = opt.insertionSort(list)
print('insertion sort: %s' % sorted_list)

sorted_list = opt.mergeSort(list)
print('merge sort: %s' % sorted_list)

sorted_list = opt.quickSort(list)
print('quick sort: %s' % sorted_list)

sorted_list = opt.countingSort(list, 100)
print('counting sort: %s' % sorted_list)

sorted_list = opt.heapSort(list)
print('heap sort: %s' % sorted_list)

