from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1c"
points = 2
@test_case()
def test_q1c(env):
    variances = env["Question1c"].variances
    assert_almost_equal(variances.mean(), 0.455 , places=2)
    assert_almost_equal(variances.var(), 0.646 , places=2)
