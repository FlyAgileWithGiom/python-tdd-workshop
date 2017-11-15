import pytest


# ---- tests there's a list---- #
def test_return_something():
    assert count_til_100() is not None


def test_return_a_list():
    # given
    # when
    result = count_til_100()
    # then
    assert isinstance(result, list)


def test_return_a_100_list():
    # given
    # when
    result = count_til_100()
    # then
    assert len(result) == 100

def test_first_is_1():
    # given
    # when
    result = count_til_100()
    # then
    assert result[1] == 1

def test_2nd_is_2():
    # given
    # when
    result = count_til_100()
    # then
    assert result[2] == 2

def test_first_is_1():
    # given
    # when
    result = say(1)
    # then
    assert result == 1

def test_2nd_is_2():
    # given
    # when
    result = say(2)
    # then
    assert result == 2

# ---- the code ---- #
def count_til_100():
    results = []
    for n in range(0,100):
        results.append(say(n))
    return results


def say(number):
    return number
