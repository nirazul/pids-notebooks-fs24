from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 1c"
points = 2
@test_case()
def test_q1c(env):
    q1c = env["Question1c"]
    assert_is_instance( q1c.increase_2021, float)
    assert_is_instance(q1c.difference_null_hypothesis, float)
    assert_almost_equal(q1c.increase_2021, 0.57142857, places=2)
    assert_almost_equal(q1c.difference_null_hypothesis, 0.0714285, places=2)
    
    
  