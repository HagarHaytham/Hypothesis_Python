from hypothesis import given
from hypothesis import assume
import hypothesis.strategies as st
import hypothesis.extra.numpy as hnp
import numpy as np
from linear import SolveGaussSeidel, SolveSOR, CheckDiagDominant,MakeItDiagDominant

#NOTE: if unique is not specified, all elements are the same.
#NOTE: using hypothesis strategies and assumptions is not very useful in this case, because we can't generate inputs and outputs that are unrelated.

@given( l= hnp.arrays(np.integer, (3,3), elements=st.integers(1,10),unique = True))
def test_diag_dominant(l):
    assert CheckDiagDominant(MakeItDiagDominant(l)) == True

@given( l= hnp.arrays(np.integer, (3,3), elements=st.integers(1,10),unique= True), x =hnp.arrays(np.integer, (3,1), elements=st.integers(1,10),unique = True))
def test_SolveGaussSeidel(l,x):
    # assume(np.linalg.matrix_rank(l) == 3)
    # sln1 = np.linalg.solve(l,x)
    # sln2,error = SolveGaussSeidel(l,x,[0,0,0],0.0001)

    A = np.array([[4,-1,-1],[-2,6,1],[-1,1,7]])
    x = np.array([3,9,-6])
    sln1 = np.linalg.solve(A,x)
    sln2,error = SolveGaussSeidel(A,x,[0,0,0],0)

    assert sln1[0] == sln2[0] and sln1[1] == sln2[1] and sln1[2] == sln1[2]
    pass    



@given( l= hnp.arrays(np.integer, (3,3), elements=st.integers(1,10),unique= True), x =hnp.arrays(np.integer, (3,1), elements=st.integers(1,10),unique = True), omega )
def test_SolveSOR(l,x):
    # assume(np.linalg.matrix_rank(l) == 3)
    # sln1 = np.linalg.solve(l,x)
    # sln2,error = SolveGaussSeidel(l,x,[0,0,0],0.0001)

    A = np.array([[3,-1,1],[-1,3,-1],[1,-1,3]])
    x = np.array([-1,7,-7])
    sln1 = np.linalg.solve(A,x)
    sln2,error = SolveSOR(A,x,[0,0,0],1.25,0)

    assert sln2[0] == 1 and sln2[1] == 2 and sln2[2] == -2
    pass    

if __name__ == "__main__":
    test_diag_dominant()
    test_SolveGaussSeidel()
    test_SolveSOR()