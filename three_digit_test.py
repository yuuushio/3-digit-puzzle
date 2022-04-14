import pytest
import three_dig as t

def test_gen_zero_th_digit():
    node = t.Node(320)
    zero_i_c = t.gen_ith_children(node, 0)
    assert (zero_i_c[0].value, zero_i_c[1].value) == (220, 420)

def test_zero_th_nine():
    node = t.Node(920)
    a = t.gen_ith_children(node, 0)
    # should only generate 1 child, since
    # you cant add to 9
    assert len(a) = 1

def test_zero_th_nine_value():
    node = t.Node(920)
    a = t.gen_ith_children(node, 0)
    assert a.[0].value == 820

def test_gen_first_index():
    node = t.Node(320)
    a = t.gen_ith_children(node, 1)
    assert (a[0].value, a[1].value) == (310, 330)

def test_gen_third_digit():
    node = t.Node(320)
    a = gen_ith_children(node, 2)
    # also tests "cant subtract from 0" functionality
    assert len(a) = 1

def test_gen_third_digit_value():
    node = t.Node(320)
    a = gen_ith_children(node, 2)
    assert (a[0].value) = (321)
