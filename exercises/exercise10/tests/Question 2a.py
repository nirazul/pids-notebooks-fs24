from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2a"
points = 2
@test_case()
def test_q2a(env):
   X_scaled = env["Question2a"].X_scaled
   assert_almost_equal(1, X_scaled.std(axis=0).mean(), 1)
      
  