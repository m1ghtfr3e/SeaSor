from SeaSor import Sort
from SeaSor import Search

# Sorting methods
def SeSortQuick(array):

    return Sort().quick(array)

def SeSortBubble(array):

    return Sort().bubble(array)

def SeSortShell(array):
    
    return Sort().shell(array)

# Searching methods
def SearchSoHash(array, target):

    return Search().hash_index(array, target)
    
def SearchSoBin(array, target):

    return Search().bin_index(array, target)

def SearchSoLin(array, target):

    return Search().lin_index(array, target)



if __name__ == '__main__':
    
    array = [5,6,7,3,4,5,7,8]
    SeSortQuick(array)
