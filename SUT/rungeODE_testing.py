from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import hypothesis.extra.numpy as hnp
from hypothesis import assume, settings


from rungeODE import Runge_kutte_ODE

#NOTE : can't generate an equation string.
#NOTE : this type of problems can't be solved using generated input, because of the need for customized input.

@given(x = st.integers())

def test_Runge_kutte_ODE(x):

    r = Runge_kutte_ODE(0,2,0,0.5,"4*(exp(0.8*x))-0.5 * y","5* (exp(0.8*x))-0.25 * (y**2)")
    output = "{:.4f}".format(r.ya)
    assert float(output) == 3.7517


if __name__ == "__main__":
    test_Runge_kutte_ODE()
    