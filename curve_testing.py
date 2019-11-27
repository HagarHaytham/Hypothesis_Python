from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from curve import curve_fitting


@given(s=text())
@example([])
def test_curve_fitting(s):
    pass    

