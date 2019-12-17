
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
    result = np.round(result,4)
    trap = np.round(trap, 4)
    # print("result >", result , trap)
    assert  result == trap

