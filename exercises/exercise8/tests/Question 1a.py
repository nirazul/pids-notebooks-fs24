from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1a"
points = 2
@test_case()
def test_q1a(env):
    x = env["Question1a"].x
    m = env["Question1a"].m
    mean = env["Question1a"].mean
    assert_equal(len(x), m)
    assert_almost_equal(mean.mean(), 9.983 , places=2)
    assert_almost_equal(mean.std() , 0.836 , places=2)
  

