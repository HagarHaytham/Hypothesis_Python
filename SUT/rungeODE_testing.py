from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from rungeODE import Runge_kutte_ODE

#NOTE : can't generate an equation string.
#NOTE : this type of problems can't 
@given(s=st.text())
def test_Runge_kutte_ODE(s):

    r = Runge_kutte_ODE(0,2,0,0.5,"4*(exp(0.8*x))-0.5 * y","5* (exp(0.8*x))-0.25 * (y**2)")
    print(r.ya)
    assert r.ya == r.ya
    pass    

if __name__ == "__main__":
    test_Runge_kutte_ODE()