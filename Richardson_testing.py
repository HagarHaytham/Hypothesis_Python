from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from Richardson import Rich


@given(s=text())
@example([])
def test_Rich(s):
    pass    

