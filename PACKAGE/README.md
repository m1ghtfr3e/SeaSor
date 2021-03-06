---

### Search and Sort Modules

---


Different Search and Sort algorithms
are implemented.


For now the functionality is really basic
but it should evolve to a collection of
several methods for searching elements 
and / or sorting sequences.


HowTo:

##### Available Sorting algorithms:

1) Bubble Sort
2) Quick Sort
3) Shell Sort

##### Available Searching algorithms:
(returns index or False if element not found)

1) Binary Search 
2) Hashmap
3) Linear Search

##### Extra features:

1)
Creating a random array.
- first parameter: length of array
- second parameter: range of numbers

Be aware that a tuple is returned, 
containing the array and a random chosen
number of this array.

```python
    
    from SeaSor import SeaSor
    
    SeaSor().get_int_array(length, range)
```

 1.1) also available for ascii array:

```python

    from SeaSor import SeaSor
     
    SeaSor().get_ascii_array(length, charset)
```

2) Remove duplicates

```python
    from SeaSor import Search
    
    # For example you want to remove duplicates
    #    before searching the index:
    
    Search().rm_dupls([1,1,2,3])
    
    # Output: [1,2,3]
```

3) Write to (and/or Read) file

***Following***

##### How to import

1) find index number of a element in a list
  (here the binary search method is applied)
    
```python
    from SeaSor import SeaSor
    
    get_index = SeaSor.Search().bin_index(array, target)
```

---
##### Create an instance

Example:

```python
    from SeaSor import Sort

    x = Sort
    
    # Possible to set parameters for the object
    # Also possible: Sort().quick([2,3,1])
    # Or:            Sort([2,3,1]).quick()
    
    x.array = [2,3,1]
    x.quick(x)

    # Output: [1,2,3]
```
---


##### Available classes

```python
    from SeaSor import SeaSor
    from SeaSor import Sort
    from SeaSor import Search
    from SeaSor import WriteRead
```



##### For more informations and instructions visit:

[SeaSor Github Repository](https://github.com/m1ghtfr3e/SearchSort)


