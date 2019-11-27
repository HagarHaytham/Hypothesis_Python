from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from gInteg import Integration_GaussLegendre


@given(s=text())
@example([])
def test_Integration_GaussLegendre(s):
    pass    
