from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from linear import SolveGaussSeidel, SolveSOR


@given(s=text())
@example([])
def test_SolveGaussSeidel(s):
    pass    

@given(s=text())
@example([])
def test_SolveSOR(s):
    pass