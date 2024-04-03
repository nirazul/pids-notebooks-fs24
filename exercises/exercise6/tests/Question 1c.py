from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1c"
points = 1

@test_case()
def test_probabilities(env):
    p_le10 = env["Question1c"].p_le10
    p_le8 = env["Question1c"].p_le8
    p_le20 = env["Question1c"].p_le20
    p_le12 = env["Question1c"].p_le12
    
    assert_almost_equal(p_le10 - p_le8, 0.336 , places=2)
    assert_almost_equal((p_le12 - p_le20)/p_le8 , -0.522 , places=2)