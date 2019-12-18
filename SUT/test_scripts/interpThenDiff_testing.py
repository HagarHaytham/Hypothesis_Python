from hypothesis import given, assume
import hypothesis.strategies as st
import hypothesis.extra.numpy as hnp
import numpy as np
import random

from interpolationDiff import differentiate


@given(x= hnp.arrays(np.integer,hnp.array_shapes(min_dims=1,max_dims=1,min_side=2, max_side=1000),elements=st.integers(1,1000),unique = True), y= hnp.arrays(np.integer,hnp.array_shapes(min_dims=1,max_dims=1,min_side=2, max_side=1000),elements=st.integers(1,1000),unique = True), val = st.integers(1,1000))
def test_newtonGeneral(x,y,val):
    
    #assume(x.shape == y.shape)
    #assume causes error in case if it's filtering  a lot of test input.
    #print(min(x.shape[0],y.shape[0]))
    vector_Size = min(x.shape[0],y.shape[0])
    print(vector_Size)
    vec_1 = x[0:vector_Size]
    vec_2 = y[0:vector_Size]

    order = random.randint(1,vector_Size-1)
    differentiate(x,True,order,0.5)

    #assert vec_1.shape[0] == vec_2.shape[0]
    pass    

if __name__ == "__main__":
    test_newtonGeneral()
