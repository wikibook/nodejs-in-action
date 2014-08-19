import time
import linear_search_1
import linear_search_2
import linear_search_3

def time_it(search, v, L):
    '''Time how long it takes to run function search to find value v in list L.'''
    
    t1 = time.time()
    search(v, L)
    t2 = time.time()

    return (t2 - t1) * 1000.

def print_times(v, L):
    '''Print the number of milliseconds it takes for linear_search(v, L) 
    to run for list.index, basic linear search, the for loop linear search, 
    and sentinel search.'''

    # Get list.index's running time.
    t1 = time.time()
    L.index(v)
    t2 = time.time()
    index_time = (t2 - t1) * 1000.    
    # Get the other three running times.
    basic_time = time_it(linear_search_1.linear_search, v, L)
    for_time = time_it(linear_search_2.linear_search, v, L)
    sentinel_time = time_it(linear_search_3.linear_search, v, L)
    
    print "%d\t%.02f\t%.02f\t%.02f\t%.02f" % \
        (v, basic_time, for_time, sentinel_time, index_time)

L = range(1000001)
linear_search_1.linear_search(10, L)
print_times(10, L)
print_times(500000, L)
print_times(1000000, L)
