from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from euler import Euler, heun


@given(s=text())
@example([])
def test_Euler(s):
    pass    

@given(s=text())
@example([])
def test_heun(s):
    pass