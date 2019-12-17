from hypothesis import given
import hypothesis.strategies as st
from hypothesis import assume
import hypothesis.extra.numpy as hnp
import numpy as np
from integ import trapezoidal,simpson_3_8,simpson_1_3
import sympy
from sympy.utilities.lambdify import lambdify, implemented_function

@given(xs=st.lists(st.floats(0,10), min_size=2, max_size=2), n=st.integers(1,10))
def test_trapezoidal(xs,n):
    Ys = []
    Xs = []
    a = min(xs[0], xs[1])
    b = max(xs[0], xs[1])
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
    # print("x & y", Xs, Ys)
    trap = np.trapz(Ys, Xs)
    try: 
        result, _ = trapezoidal(func, a, b, n)
    except ZeroDivisionError:
        # print ("error division by zero")
        result = -1
    
    result = "{0:.4f}".format(result)
    trap = "{0:.4f}".format(trap)
    # print("result >", result , trap)
    assert  result == trap


@given(s = st.text())
# @example([])
def test_simpson_3_8(s):
    pass

@given(s = st.text())
# @example([])
def test_simpson_1_3(s):
    pass

if __name__ == "__main__":
    test_trapezoidal()