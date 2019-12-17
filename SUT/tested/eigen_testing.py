from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from eigen import powerMethod, deflate


@given(s=text())
@example([])
def test_power_method(s):
    eigen_value , eigen_vector = powerMethod(s)
    assert np.dot(A , eigen_vector) == eigen_value * eigen_vector
    
@given(s=text())
@example([])
def test_deflate(s):
    pass