from sort4 import selection_sort
import nose

def run_test(original, expected):
    '''Sort list original and compare it to list expected.'''
    selection_sort(original)
    assert original == expected

def test_empty():
    '''Test sorting empty list.'''
    run_test([], [])

def test_one():
    '''Test sorting a list of one value.'''
    run_test([1], [1])

def test_two_ordered():
    '''Test sorting an already-sorted list of two values.'''
    run_test([1, 2], [1, 2])

def test_two_reversed():
    '''Test sorting a reverse-ordered list of two values.'''
    run_test([2, 1], [1, 2])

def test_three_identical():
    '''Test sorting a list of three equal values.'''
    run_test([3, 3, 3], [3, 3, 3])

def test_three_split():
    '''Test sorting a list with an odd value out.'''
    run_test([3, 0, 3], [0, 3, 3])

if __name__ == '__main__':
    nose.runmodule()
