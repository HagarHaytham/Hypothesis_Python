from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from SODE import SolveODE


@given(s=text())
@example([])
def test_SolveODE(s):
    pass    

