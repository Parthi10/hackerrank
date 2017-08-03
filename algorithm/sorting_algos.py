from random import shuffle
from time import time

class Sort(object):

    def __init__(self, array):
        self.array = array

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    def selection_sort(self, array):
        for i in range(len(array)-1):
            min_index = i#index with minimum number
            for j in range(i+1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            #swap ith element with min of array[i:]
            self.swap(i, min_index, array)

        return array

    def bubble_sort(self, array):
        for k in range(1, len(array)):
            already_sorted = True
            #will put max at last_index for sure
            for j in range(len(array)-k):
                if array[j] > array[j+1]:
                    already_sorted = False
                    self.swap(j, j+1, array)
            if already_sorted:
                break

        return array

    def insertion_sort(self, array):
        for boundary in range(1, len(array)):
            hole = boundary
            element = array[boundary]
            while hole>0 and array[hole-1] > element:
                array[hole] = array[hole-1]
                hole-=1
            array[hole] = element

        return array

        '''
        alternate swapping method, takes twice as much time,
        lesson to be learnt: swapping is shit (remember bubble sort?)
        '''
        # for i in range(1, len(array)):
        # hole = i
        # while hole>0 and array[hole-1] > array[hole]:
        #     swap(array, hole, hole-1)
        #     hole -= 1
        # return array

    def merge(self, L, R, array):
        nL, nR = len(L), len(R)
        l, r, i = 0, 0, 0

        while l<nL and r<nR:
            if L[l] <= R[r]:
                array[i] = L[l]; l += 1
            else:
                array[i] = R[r]; r += 1
            i+=1

        while l<nL:
            array[i] = L[l]
            l+=1; i+=1

        while r<nR:
            array[i] = R[r]
            r+=1; i+=1

        return array

    def merge_sort(self, array):
        if len(array)==1:
            return array
        L = array[:len(array)//2]
        R = array[len(array)//2:]
        L = self.merge_sort(L)
        R = self.merge_sort(R)

        return self.merge(L, R, array)

    def pypartition(self, start, end, array):#pythonic partition
        #less efficient than partition
        pivot = end
        i = start
        while i<pivot:
            if array[i] > array[pivot]:
                array.append(array.pop(i))
                pivot-=1
            else:
                i+=1
        return pivot

    def partition(self, start, end, array):
        pivot = end
        pIndex = start
        #elem>array[pivot] will be come left of pIndex and vice versa for <
        for i in range(start, end):
            if array[i] <= array[pivot]:# '=' is v. imp
                self.swap(i, pIndex, array)
                pIndex += 1
        self.swap(pIndex, pivot, array)
        return pIndex

    def quick_sort(self, start, end, array):
        if start >= end:
            return
        pivot = self.partition(start, end, array)
        self.quick_sort(start, pivot-1, array)
        self.quick_sort(pivot + 1, end, array)

        return array

    def run(self, array):
        start = time()
        a = self.selection_sort(array[:])
        print('time taken selection_sort: %0.10f' %(time()-start))
        print(a[:10])

        start = time()
        a = self.bubble_sort(array[:])
        print('time taken bubble_sort: %0.10f' %(time()-start))
        print(a[:10])

        start = time()
        a = self.insertion_sort(array[:])
        print('time taken insertion_sort: %0.10f' %(time()-start))
        print(a[:10])

        start = time()
        a = self.merge_sort(array[:])
        print('time taken merge_sort: %0.10f' %(time()-start))
        print(a[:10])

        start = time()
        a = self.quick_sort(0, len(array)-1, array[:])
        print('time taken quick_sort: %0.10f' %(time()-start))
        print(a[:10])

array = list(range(10000))
shuffle(array)
print(array[:10])
print('array ready\n')

sort = Sort(array)
sort.run(array)
