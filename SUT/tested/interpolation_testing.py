from hypothesis import given, example
import hypothesis.strategies as st
import numpy as np
from scipy import interpolate
from interpolation import interpolateNewton, interpolationLagrange
import sympy
from sympy.utilities.lambdify import lambdify, implemented_function


@st.composite 
def generate_list(draw):
    
    
    Xs = draw(st.lists(st.decimals(0,10,places=2), min_size=4, max_size=4, unique=True).map(sorted))
    Ys = draw(st.lists(st.decimals(0,10,places=2), min_size=4, max_size=4, unique=True).map(sorted))
    new_x = draw(st.floats(min(Xs),max(Xs)))
    Xs = [float(i) for i in Xs]
    Ys = [float(i) for i in Ys]
    return Xs, Ys, new_x

@given(l =generate_list()) 
def test_interpolationLagrange(l):
    Xs = l[0]
    Ys = l[1]
    new_x = l[2]
    _, val = interpolationLagrange(Xs,Ys,new_x)
    yn = interpolate.barycentric_interpolate(Xs,Ys, new_x)
    assert np.round(val,3) == np.round(yn,3)
    # lag = interpolate.lagrange(Xs,Ys)
    # assert np.round(val,3) == np.round(lag(new_x),3)

@given(s=st.text())
def test_interpolateNewton(s):
    Xs = [1,4,6,5,7]
    Ys = [0,1.386294,1.791759,1.609438,1.82]
    new_x = 3
    _, val = interpolateNewton(Xs, Ys, x0=new_x)
    yn = interpolate.barycentric_interpolate(Xs,Ys, new_x)
    assert np.round(val,3) == np.round(yn,3)   


if __name__ == "__main__":
    test_interpolationLagrange()
    test_interpolateNewton()