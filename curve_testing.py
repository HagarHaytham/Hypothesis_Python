from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from curve import curve_fitting

def fun1(x):
    return x ** 4 + x ** 3 + x ** 2 + x  ** 1 +6565656

x = list(range(100))
y = list(map(fun1, x))
actual = curve_fitting(x,y,degree=4)
expected =np.polyfit(x, y, 4)
print(actual)
print(expected)
for i in range(len(actual)):
    print(i,actual[i]==expected[i])
if actual.all() == expected.all():
    print("eeh")

a = 3.4536
b="{0:.1f}".format(a)
print(b)

# @given(s=text())
# @example([])
# def test_curve_fitting(s):
#     pass    

