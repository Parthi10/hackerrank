from random import shuffle
from time import time

class Sort(object):

    def __init__(self, array):
        self.array = array

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    def selection_sort(self, array):
        for i in range(len(array)-1):
            min_i = i
            for j in range(i+1, len(array)):
                if array[j] < array[min_i]:
                    min_i = j
            self.swap(min_i, i, array)
        return array

    def bubble_sort(self, array):
        for i in range(len(array)):
            flag = True
            for j in range(len(array)- i -1):
                if array[j] > array[j+1]:
                    self.swap(j, j + 1, array)
                    flag = False
            if flag:
                break
        return array

    def insertion_sort(self, array):
        pointer = 1
        while pointer < len(array):
            element = array[pointer]
            hole = pointer
            while hole > 0 and array[hole - 1] > element:
                array[hole] = array[hole - 1]
                hole -= 1
            array[hole] = element
            pointer += 1
        return array

    def merge(self, array1, array2):
        newArray = []
        i, j = 0, 0
        while i < len(array1) and j < len(array2):
            if array1[i] < array2[j]:
                newArray.append(array1[i])
                i += 1
            else:
                newArray.append(array2[j])
                j += 1
        if i < len(array1):
            newArray.extend(array1[i:])
        elif j < len(array2):
            newArray.extend(array2[j:])
        return newArray

    def merge_sort(self, array):
        if len(array) == 1:
            return array
        array1 = self.merge_sort(array[:len(array)//2])
        array2 = self.merge_sort(array[len(array)//2:])

        array = self.merge(array1, array2)
        return array

    def getPivotIndex(self, array, start, end):
        pivotElement = array[end]
        dummyIndex = start
        for i in range(start, end):
            if array[i] < pivotElement:
                 if dummyIndex != i:
                     self.swap(i, dummyIndex, array)
                 dummyIndex += 1

        self.swap(dummyIndex, end, array)
        return dummyIndex


    def quick_sort(self, array, start, end):
        if start >= end:
            return
        pivot = self.getPivotIndex(array, start, end)
        self.quick_sort(array, start, pivot-1)
        self.quick_sort(array, pivot+1, end)
        return array

    def run(self, array):
        start = time()
        a = self.selection_sort(array[:])
        print('\ntime taken selection_sort: %0.10f' %(time()-start))
        print(a[:10])

        start = time()
        a = self.bubble_sort(array[:])
        print('\ntime taken bubble_sort: %0.10f' %(time()-start))
        print(a[:10])

        start = time()
        a = self.insertion_sort(array[:])
        print('\ntime taken insertion_sort: %0.10f' %(time()-start))
        print(a[:10])
        #
        start = time()
        a = self.merge_sort(array[:])
        print('\ntime taken merge_sort: %0.10f' %(time()-start))
        print(a[:10])

        start = time()
        a = self.quick_sort(array, 0, len(array)-1)
        print('\ntime taken quick_sort: %0.10f' %(time()-start))
        print(a[:10])

length = 100
print("creating an array of length : %d " % length)
array = list(range(length))
shuffle(array)
print(array[:10])
print('array ready\n')

sort = Sort(array)
sort.run(array)
