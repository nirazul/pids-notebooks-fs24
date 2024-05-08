from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 1c"
points = 2
@test_case()
def test_q1c(env):
    r2 = env["Question1c"].r2
    lb = 0.4
    ub = 0.6
    
    assert_true(lb <= r2 <= ub)
    
    
  