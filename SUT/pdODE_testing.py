from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from pdODE import PredictorCorrector

@st.composite 
def generate_input(draw):
    initial_x= draw(st.floats(min_value = 0 ,max_value = 10))
    initial_y=draw (st.floats(min_value = 0 ,max_value = 10))
    intervals=draw(st.integers(min_value = 2 ,max_value = 10))
    stopping_x=draw(st.floats(min_value = 0 ,max_value = 10))
    exp =draw(st.from_regex("([+-][1-9]{1,1}([m][x][p][1-9]{1,1})([m][c][o][s][(][x][)]){0,1}([m][s][i][n][(][x][)]){0,1}){1,2}([+-][1-9]{1,1}([m][y][p][1-9]{1,1})([m][c][o][s][(][y][)]){0,1}([m][s][i][n][(][y][)]){0,1}){1,2}",fullmatch=True))
    return initial_x,initial_y,intervals,stopping_x,exp

@given(input=generate_input())
@example(input)
def test_PredictorCorrector(s):
    
    pass    
