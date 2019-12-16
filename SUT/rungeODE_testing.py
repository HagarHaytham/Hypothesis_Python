from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import hypothesis.extra.numpy as hnp
from hypothesis import assume


from rungeODE import Runge_kutte_ODE

#NOTE : can't generate an equation string.
#NOTE : this type of problems can't 
@given(s=st.text())
def test_Runge_kutte_ODE(s):

    r = Runge_kutte_ODE(0,2,0,0.5,"4*(exp(0.8*x))-0.5 * y","5* (exp(0.8*x))-0.25 * (y**2)")
    print(r.ya)
    assert r.ya == r.ya
    pass

def randomize_size():
    return st.integers(1,10)


@given( l= hnp.arrays(np.integer,hnp.array_shapes(min_dims=2, max_dims=2) ,elements=st.integers(1,100),unique = True))
def test_rand(l):
    assume(l.shape[1] == 2)
    print(l.shape)
    

    pass


if __name__ == "__main__":
    #test_Runge_kutte_ODE()
    #print(randomize_size())
    test_rand()
    #print(i)