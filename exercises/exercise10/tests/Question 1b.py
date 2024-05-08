from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 1b"
points = 2
@test_case()
def test_q1a(env):
    y_pred = env["Question1b"].y_pred
    
    t_stddev = 54
    t_mean = 151
    assert_true((np.abs(y_pred.std() - t_stddev) < 3) and np.abs(y_pred.mean() - t_mean) < 5 )
   