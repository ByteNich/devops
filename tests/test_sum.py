from main import summ

def test_pos_sum():
    assert summ(1, 2) == 3

def test_neg_sum():
    assert summ(-1, 2) == 1
    