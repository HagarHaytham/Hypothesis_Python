from hypothesis import given,assume
import hypothesis.extra.numpy as hnp
import hypothesis.strategies as st
import numpy as np
import random
from scipy import integrate
from Richardson import Rich

# global i
# @given(m=hnp.arrays(np.integer,hnp.array_shapes(min_dims=2,max_dims=2,min_side=2, max_side=5),elements=st.integers(1,100),unique=True))
@given(dx=st.floats(0.5,2),y =hnp.arrays(np.float,st.integers(5,10),elements=st.floats(1,6),unique=True))
def test_Rich(dx,y):

    # assume(m.shape[0]==2) # i want 2 vectors only
    y.sort()
    y=list(y)
    # print(y)
    x=[1]
    for i in range (len(y)-1):
        x.append(x[i]+dx)
    # x=np.array(x)
    table = [x,y]
    # print(table)
    idx = random.randint(0,len(x)-1)
    _,actual=Rich(x[idx],table)
    expected=integrate.romb(y,dx)
    assert actual == expected
    i+=1
    # print(type(table))
    # pass    
if __name__=="__main__":
    test_Rich()
