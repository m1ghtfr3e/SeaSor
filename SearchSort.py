import random

class SearchSort:

    '''
        this class mainly provides 
        searching & sorting methods
        one method can create list
          with random numbers and
          optional parameters
    '''

    def __init__(self, array = None, targetnum = None):

        self.array = array
        self.targetnum = targetnum

    def quick_sort_array(self, array=None):

        ''' private class method
            sorts an array
            can take the self or 
            an optional parameter
        '''
        # if no func parameter, take self.*
        if array == None:
            array = self.array

        #recursive method
        def sort_my_array(array):

            '''
                nested func so we do
                not have to care about
                self or optional parameter
            '''
            if len(array) <= 1:
                return array
            else:
                pivot = array.pop()

                smaller = []    # smaller than pivot
                bigger = []     # bigger than pivot

            for i in array:
                if i < pivot:
                    smaller.append(i)
                else:
                    bigger.append(i)
            return sort_my_array(smaller) + [pivot] + sort_my_array(bigger)

        return sort_my_array(array)

    def binary_search_indexarray(self, array=None, target=None):

        ''' binary search method
            recursively
            needs sorted list
            returns falls if item not in list
        '''
        if array == None:
            array = self.array
            target = self.targetnum

        start, end = 0,  (len(array)-1)
        found = False
        while start <= end and not found:
            mid = ((start + end) // 2)
            if array[mid] == target:
                found = True
                return mid
            elif target < array[mid]:
                end = mid - 1
            elif target > array[mid]:
                start = mid + 1
        return False

    def hash_search_indexarray(self, array = None, target = None):
        
        ''' search in hashmap
            checks value for value
            returns false if item not in list
        '''
        if array == None:
            array = self.array
            target = self.targetnum

        for _ in range(len(array)):
            for p, n in enumerate(array):
                if n == target:
                    return p
        return False

    def linear_search_indexarray(self, array, target):

        '''
            iterates over positions
            one by one and returns postion
            if found, otherwise false
        '''
        if array == None:
            array = self.array
            target = self.targetnum

        for pos in range(len(array)):
            if array[pos] == target:
                return pos
        return False
    
    def get_int_array(self, length=100):

        ''' creates arrays with
            optional length and 
            random numbers
            return also a random
            choice of the created
            list to test previous
            methods
        '''
        rand_array = []

        for i in range(length):
            n = random.randrange(length)
            rand_array.append(n)

        include_num = random.choice(rand_array)

        return rand_array, include_num
