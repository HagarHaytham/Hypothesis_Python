from hypothesis import given , assume
import hypothesis.strategies as st
import numpy as np
from sympy.solvers.pde import pdsolve
from sympy import Function, diff, Eq
from sympy.abc import x, y
from pdODE import PredictorCorrector
# def PredictorCorrector(Xpoints,Ypoints,equation,technique,xs,ApproxError):
import sympy
from sympy.utilities.lambdify import lambdify, implemented_function 

@st.composite 
def generate_input(draw):
    exp =draw(st.from_regex("([+-][1-9]{1,1}([m][x][p][1-9]{1,1})([m][c][o][s][(][x][)]){0,1}([m][s][i][n][(][x][)]){0,1}){1,2}([+-][1-9]{1,1}([m][y][p][1-9]{1,1})([m][c][o][s][(][y][)]){0,1}([m][s][i][n][(][y][)]){0,1}){1,2}",fullmatch=True))
    x = draw(st.floats(allow_nan=False,allow_infinity=False))
    step =draw(st.floats(min_value = 0 , max_value = 1))
    assume (step > 0)
    n = draw(st.integers(min_value = 5 , max_value = 10))
    Ys = draw(st.lists(st.floats(allow_nan=False,allow_infinity=False), min_size=n, max_size=n, unique=True).map(sorted))
    Xs = []
    for i in range(n):
        Xs.append(x+i*step)
    xs=[]
    xs.append(Xs[n-1]+step)
    approx_error = draw(st.floats( min_value = 0 , max_value = 0.1))
    technique = draw(st.integers(min_value = 0 ,max_value = 3))
    # print(Xs)
    return Xs, Ys, exp , technique,xs,approx_error

@given(input=generate_input())
def test_PredictorCorrector(input):
    Xs = input[0]
    Ys = input[1]
    exp= input[2]
    technique= input[3]
    xs= input[4]
    approx_error= input[5]
    exp = exp.replace('m','*')
    exp = exp.replace('p','**')
    exp =exp [1:len(exp)] 
    try:    
        f = sympy.sympify(exp)
    except:
        print('sympify error')
        pass
    # print(f)
    # print(exp)
    try:
        ys ,errors,finalerror = PredictorCorrector(Xs, Ys, str(f) , technique,xs,approx_error)
    except :
        pass
    x = sympy.symbols('x')
    y = sympy.symbols('y')
    # try:
    #     # fx = lambdify([x,y] , f)
    #     # print(fx)
    # except:
    #     print('lambdify error')
        # pass
    ux = sympy.diff(f,x)
    uy = sympy.diff(f,y)
    eq = Eq(1 + (2*(ux/f)) + (3*(uy/f)), 0)
    try:
        sol = pdsolve(eq)
        print(sol)
    except:
        pass
    # ux = sympy.sympify()
    pass    

if __name__ == "__main__":
    test_PredictorCorrector()
