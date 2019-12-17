from hypothesis import given
import hypothesis.strategies as st
from hypothesis import assume
import hypothesis.extra.numpy as hnp
import numpy as np
from integ import trapezoidal,simpson_3_8,simpson_1_3
import sympy
from sympy.utilities.lambdify import lambdify, implemented_function
from scipy import integrate

@st.composite
def generate_function(draw):
    Xs = []
    Ys = []
    p = draw(st.lists(st.floats(0,10), min_size=2, max_size=2))
    n = draw(st.integers(1,10))
    a = min(p[0], p[1])
    b = max(p[0], p[1])
    a=0
    b=0.8
    func =  '0.2 + 25 * x - 200 * x * x + 675 * x**3 - 900 * x**4 + 400 * x**5'
    f = sympy.sympify(func)
    x = sympy.symbols('x')
    fx = lambdify(x, f)
    temp_x = a
    temp_y = fx(temp_x)
    Ys.append(temp_y)
    Xs.append(temp_x)
    h = (b-a) / n
    while temp_x + h < b:
        temp_y = fx(temp_x + h)
        temp_x = temp_x + h
        Ys.append(temp_y)
        Xs.append(temp_x)
    if a != b:
        Xs.append(b)
        Ys.append(fx(b))
    return func, Xs, Ys, a, b, n

@given(l=generate_function())
def test_trapezoidal(l):
    func = l[0]
    Xs = l[1] 
    Ys = l[2]
    a = l[3]
    b = l[4]
    n = l[5]
    trap = np.trapz(Ys, Xs)
    # try: 
    result, _ = trapezoidal(func, a, b, n)
    # except ZeroDivisionError:
    #     print ("error division by zero")
    #     result = -1
    result = np.round(result,4)
    trap = np.round(trap, 4)
    assert  result == trap


@given(l=generate_function())
def test_simpson_3_8(l):
    func = l[0]
    Xs = l[1] 
    Ys = l[2]
    a = l[3]
    b = l[4]
    I, _ = simpson_3_8(func, a, b)
    assert np.round(I,3) == 1.519

if __name__ == "__main__":
    test_trapezoidal()
    test_simpson_3_8()
