from hypothesis import strategies as st
from hypothesis import given,example,assume


#applying the concept of property based testing.
def add(x,y):
    return x+y

@given(x = st.integers(), y = st.integers())
def test_add(x,y):
    assert add(x,y) == add(y,x)

def encode(input_string):
    # the following two lines were added after running test, and discovering a failure in case of an empty string.
    if input_string == "":
        return []
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

@given(s = st.text())
@example(s = "")
def test_encode_decode(s):
    assert decode(encode(s)) == s

#testing Assume
#in this function, it asserts that the sum of elements in a positive array is definitely positive.
@given(st.lists(st.integers(1,1000)))
def test_sum_is_positive(xs):
    assume(len(xs)>0)
    assert sum(xs) > 0    

#RUNNING TESTS.
if __name__ == "__main__":
    # test_add()
    # test_encode_decode()
    # test_sum_is_positive()

