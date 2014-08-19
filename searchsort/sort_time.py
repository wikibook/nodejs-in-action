import time
from sort4 import selection_sort
from sort7 import insertion_sort
from ms import mergesort

def built_in(L):
    '''Call list.sort --- we need our own function to do this
    so that we can treat it as we treat our own sorts.'''
    L.sort()

def print_times(L):
    '''Print the number of milliseconds it takes for selection sort
    and insertion sort to run.'''
    print len(L),
    for func in (selection_sort, insertion_sort, mergesort, built_in):
        if func in (selection_sort, insertion_sort) and len(L) > 4000:
            continue
            
        L_copy = L[:]
        t1 = time.time()
        func(L_copy)
        t2 = time.time()
        print "\t%.1f" % ((t2 - t1) * 1000.),
    print

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000]:
    L = range(list_size)
    L.reverse()
    print_times(L)
