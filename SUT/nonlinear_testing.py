from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from nonlinear import NonLinearSolver


@given(s=text())
@example([])
def test_NonLinearSolver(s):
    pass    

