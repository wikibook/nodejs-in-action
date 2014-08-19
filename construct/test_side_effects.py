import nose

numbers = [1, 3, -1, 5]

def test_max():
    assert max(numbers) == 5

def test_min():
    assert min(numbers) == -1

def test_append():
    old_len = len(numbers)
    numbers.append(99)
    assert len(numbers) == old_len + 1

if __name__ == '__main__':
    nose.runmodule()
