from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 2a"
points = 3
@test_case()
def test_q2a(env):
    CI_scipy = env["Question2a"].CI_scipy

    assert_equal(len(CI_scipy), 2)
    assert_almost_equal(CI_scipy[1] - CI_scipy[0], 0.21 , places=2)
    assert_almost_equal(np.std(CI_scipy) , 0.107 , places=2)
