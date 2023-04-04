from utils.arrs import get, my_slice
import pytest


@pytest.mark.parametrize("a, b, default", [([1, 2, 3], 1, 2),
                                          ([], 0, None),
                                          ([1, 2, 3], -1, None)])
def test_get(a, b, default):
    assert get(a, b) == default


def test_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3, 4], -2) == [3, 4]
    assert my_slice([1, 2, 3, 4], -5) == [1, 2, 3, 4]
    assert my_slice([1, 2, 3, 4], 0, 2) == [1, 2]
    assert my_slice([1, 2, 3], 1) == [2, 3]
    assert my_slice([], 1) == []
