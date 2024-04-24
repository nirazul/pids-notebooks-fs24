from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 1d"
points = 3
@test_case()
def test_q1c(env):
    q1d = env["Question1d"]
    assert_is_instance( q1d.p_value, float)
    assert_almost_equal(q1d.p_value, 0.51269, places=2)
    
    
  