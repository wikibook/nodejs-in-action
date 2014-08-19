import nose

def test_empty_list():
    assert running_sum([]) == []

def test_single_value():
    assert running_sum([1]) == [1]

	
def test_two_values():
    assert running_sum([1, 3]) == [1, 4]

def test_three_values():
    assert running_sum([1, 3, 7]) == [1, 4, 11]

def test_negative_values():
    assert running_run([-1, 1]) == [-1, 0]

def test_mixed_types():
    assert running_sum([1, 3.0]) == [1, 4.0]

def test_string():
    try:
        running_sum('string')
        assert False
    except ValueError:
        pass
    except:
        assert False

def test_non_numeric():
    try:
        running_sum(['string'])
        assert False
    except ValueError:
        pass
    except:
        assert False
