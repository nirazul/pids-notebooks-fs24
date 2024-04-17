from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 2b"
points = 1
@test_case()
def test_q2b(env):
    CI_scipy_4000 = env["Question2b"].CI_scipy_4000

    assert_equal(len(CI_scipy_4000), 2)
    assert_almost_equal(CI_scipy_4000[1] - CI_scipy_4000[0], 0.054 , places=2)
    assert_almost_equal(np.std(CI_scipy_4000) , 0.027 , places=2)