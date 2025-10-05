def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_string():
    assert "hello".upper() == "HELLO"

def test_list():
    numbers = [1, 2, 3]
    assert len(numbers) == 3
    assert numbers[0] == 1