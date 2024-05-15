from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 1b"
points = 2
@test_case()
def test_q1a(env):
    acc = env["Question1b"].accuracy
    
    assert_true(acc > 0.98)
   