from main import dif

def test_pos_dif():
    assert dif(2, 1) == 1

def test_neg_dif():
    assert dif(-5, -2) == -3
