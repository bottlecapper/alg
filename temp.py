
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
        return self.subQuickSort(list, 0, len(list)-1)

    def subQuickSort(self, list, start, end):
        if start < end:
            split = self.partition(list, start, end)
            self.subQuickSort(list, start, split-1)
            self.subQuickSort(list, split+1, end)

    def partition(self, list, start, end):
        pivot = list[start]

        leftpointer = start + 1
        rightpointer = end

        while (leftpointer <= rightpointer):
            while list[leftpointer] <= pivot and leftpointer <= rightpointer:
                leftpointer += 1

            while list[rightpointer] >= pivot and leftpointer <= rightpointer:
                rightpointer -= 1

            list[leftpointer], list[rightpointer] = list[rightpointer], list[leftpointer]

        return rightpointer




### TEST ###

opt = Solution()
list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# sorted_list = opt.insertionSort(list)
# print('insertion sort: %s' % sorted_list)
#
# sorted_list = opt.mergeSort(list)
# print('merge sort: %s' % sorted_list)
#
# sorted_list = opt.quickSort(list)
# print('quick sort: %s' % sorted_list)


