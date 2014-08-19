empty_list = []
one_item_list = ['He']
multi_item_list = ['Ne', 'Ar', 'He', 'He']

def test_remove_from_empty():
    remove_all(empty_list, 'He')
    assert len(empty_list) == 0

def test_remove_from_one_item_list():
    remove_all(one_item_list, 'He')
    assert len(one_item_list) == 0

def test_remove_something_else():
    remove_all(one_item_list, 'Pb')
    assert len(one_item_list) == 1

def test_remove_multiple():
    remove_all(multi_item_list, 'He')
    assert len(multi_item_list) == 2
