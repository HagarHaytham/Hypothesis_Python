from hypothesis import given , assume , settings ,note
import hypothesis.strategies as st
import numpy as np
import sympy
from sympy.utilities.lambdify import lambdify, implemented_function
from euler import Euler, heun
from scipy.integrate import odeint
# @settings(max_examples=1)
@st.composite 
def generate_input(draw):
    initial_x= draw(st.floats(min_value = 0 ,max_value = 10))
    
    initial_y=draw (st.floats(min_value = 0 ,max_value = 10))
    
    intervals=draw(st.integers(min_value = 2 ,max_value = 10))
    
    
    final_x=draw(st.floats(min_value = 0 ,max_value = 10))
    exp =draw(st.from_regex("([+-][1-9]{1,1}([m][x][p][1-9]{1,1})([m][c][o][s][(][x][)]){0,1}([m][s][i][n][(][x][)]){0,1}){1,2}([+-][1-9]{1,1}([m][y][p][1-9]{1,1})([m][c][o][s][(][y][)]){0,1}([m][s][i][n][(][y][)]){0,1}){1,2}",fullmatch=True))
    return initial_x,initial_y,intervals,final_x,exp

@given(data = generate_input())
def test_Euler(data):
    initial_x = data[0]
    initial_y = data[1]
    intervals = data[2]
    final_x= data[3]
    exp = data[4]
    exp = exp.replace('m','*')
    exp = exp.replace('p','**')
    exp =exp [1:len(exp)]     
    # print(str(exp))
    f = sympy.sympify(exp)
    assume(final_x > initial_x)
    assume(intervals > 0)
    y1 = Euler(exp,initial_x,initial_y,final_x,intervals)
    t=[]
    last = initial_x
    step = (final_x - initial_x )/intervals
    # print(step)
    for i in range(intervals):
        last+=step
        t.append(last)
    x = sympy.symbols('x')
    y = sympy.symbols('y')
    fx = lambdify([x,y] , f)
    # print(f)
    y2 = odeint(fx,initial_y,np.asarray(t))
    # print(len(result))
    # print(exp,initial_x,initial_y,final_x,intervals)
    # print(len(y1),len(y2))
    for i in range(len(y2)):
        note("numpy sol %r"% y2[i][0])
        note("app solution %r"%  y1[i])
        assert y2[i][0] == y1[i]
       
    
# @given()
# def test_heun():
#     pass
if __name__ == "__main__":
    test_Euler()
