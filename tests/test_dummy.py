from libtibo.dummy import flip_list, get_hello_str
import numpy as np

def test_flip_list_empty():
    assert flip_list([]) == []

def test_flip_list_one_element():
    assert flip_list([0]) == [0]
    assert flip_list(['0']) == ['0']

def test_flip_list_numpy_array():
    assert np.array_equal(
        flip_list(np.array([1, 2, 3])),
        np.array([3, 2, 1])
        )

def test_get_hello_str_empty():
    assert get_hello_str('') == 'Hello !'

def test_get_hello_str_float():
    assert get_hello_str(3.14) == 'Hello 3.14!'

def test_get_hello_str_regular():
    assert get_hello_str('Alice') == 'Hello Alice!'
