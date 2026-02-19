import numpy as np
import task7

#test creating arrays
def testCreateArray():
    arr = task7.createArray()
    assert isinstance(arr, np.ndarray)
    assert np.array_equal(arr, np.array([1, 2, 3, 4]))

#Test for correct mean
def testMean():
    arr = np.array([5, 4, 3, 2, 1])
    assert task7.mean(arr) == 3

#test for correct product
def testMultiply():
    arr = np.array([1, 2, 3])
    result = task7.multiply(arr, 3)
    assert np.array_equal(result, np.array([3, 6, 9]))
