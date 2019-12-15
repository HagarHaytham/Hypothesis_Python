from hypothesis import given
import hypothesis.strategies as st
import hypothesis.extra.numpy as hnp
import numpy as np
import linear


from linear import SolveGaussSeidel, SolveSOR, CheckDiagDominant,MakeItDiagDominant

#NOTE: if unique is not specified, all elements are the same.

@given( l= hnp.arrays(np.float, (3,3), elements=st.floats(1,10),unique = True))
def test_diag_dominant(l):
    #print("inside test.")
    print(l)
    assert CheckDiagDominant(MakeItDiagDominant(l)) == True

@given( l= hnp.arrays(np.float, (3,4), elements=st.floats(1,2),unique= True))
def test_SolveGaussSeidel(l):
    A = l[:,0:3]
    x = l[:,3]
    print(np.linalg.solve(A,x))

    pass    



# @given(st=text())
# @example([])
# def test_SolveSOR(s):

#     pass


if __name__ == "__main__":
    test_SolveGaussSeidel()