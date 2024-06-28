
from main import mul

def test_pos_mul():
    assert mul(2, 4) == 8

def test_neg_mul():
    assert mul(-5, 3) == -15
    