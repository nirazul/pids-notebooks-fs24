from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1a"
points = 1
@test_case()
def test_q1a(env):
    X = env["Question1a"].X_scaled
    y = env["Question1a"].y

    assert_equal(X.shape, (298, 30))
    assert_equal(y.shape[0], 298)

    assert_almost_equal(0, X.mean(axis=0).sum(), 1)