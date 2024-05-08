from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1a"
points = 1
@test_case()
def test_q1a(env):
    X = env["Question1a"].X
    y = env["Question1a"].y

    assert_equal(X.shape, (349, 10))
    assert_equal(y.shape[0], 349)
