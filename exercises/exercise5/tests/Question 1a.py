from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1a"
points = 1
@test_case()
def test_coin_tosses(env):
    omega_three_coin_tosses = env["Question1a"].omega_three_coin_tosses
    assert_is_instance(omega_three_coin_tosses, set)
    assert_true((0,0,0) in omega_three_coin_tosses)
    assert_true((1,1,0) in omega_three_coin_tosses)
    assert_equal(len(omega_three_coin_tosses),8)
    