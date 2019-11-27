from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from rungeODE import Runge_kutte_ODE


@given(s=text())
@example([])
def test_Runge_kutte_ODE(s):
    pass    

