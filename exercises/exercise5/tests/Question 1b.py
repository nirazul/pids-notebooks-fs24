from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1b"
points = 1
@test_case()
def test_omega(env):
    omega_same_number_twice = env["Question1b"].omega_same_number_twice
    assert_is_instance(omega_same_number_twice, set)
    assert_true((1,1) in omega_same_number_twice)
    assert_equal(omega_same_number_twice, set(((1,1), (2,2), (3,3), (4,4), (5,5), (6,6))))    
    assert_equal(len(omega_same_number_twice),6)
    