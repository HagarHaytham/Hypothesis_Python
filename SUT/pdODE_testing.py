from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from pdODE import PredictorCorrector


@given(s=text())
@example([])
def test_PredictorCorrector(s):
    pass    
