from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from interpolation import interpolateNewton, interpolationLagrange


@given(s=text())
@example([])
def test_interpolateNewton(s):
    pass    

@given(s=text())
@example([])
def test_interpolationLagrange(s):
    pass