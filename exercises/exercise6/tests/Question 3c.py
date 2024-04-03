from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 3c"
points = 1

@test_case()
def test_mean(env):
    p_le2 = env["Question3c"].p_le2
    p_gr4 = env["Question3c"].p_gr4
    p_gr2_le3 = env["Question3c"].p_gr2_le3
    
    assert_equal(p_le2 - p_gr4, 0)
    assert_almost_equal((p_gr2_le3 - p_le2)/p_gr4 , -0.379 , places=2)
    