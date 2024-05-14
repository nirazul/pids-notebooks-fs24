from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 1c"
points = 2
@test_case()
def test_q1a(env):
    acc = env["Question1c"].accuracy
    
    assert_true(0.9 < acc < 0.98)
   