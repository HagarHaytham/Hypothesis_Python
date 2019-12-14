from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from integ import trapezoidal,simpson_3_8,simpson_1_3


@given(s=text())
@example([])
def test_trapezoidal(s):
    pass    

@given(s=text())
@example([])
def test_simpson_3_8(s):
    pass

@given(s=text())
@example([])
def test_simpson_1_3(s):
    pass