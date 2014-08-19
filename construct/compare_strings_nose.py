import nose

def test_compare():
    '''Test comparison of unequal strings.'''
    
    assert my_compare('abc', 'def') == -1

if __name__ == '__main__':
    nose.runmodule()
