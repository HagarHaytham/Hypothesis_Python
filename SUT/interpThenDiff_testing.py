from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from interpThenDiff import newtonGeneral


@given(s=text())
@example([])
def test_newtonGeneral(s):
    pass    

