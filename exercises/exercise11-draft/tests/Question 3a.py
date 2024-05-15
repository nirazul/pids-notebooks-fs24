from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 3a"
points = 2
@test_case()
def test_q2a(env):
   xc = env["Question3a"].X_cleaned
   assert_true(xc.shape == (1309, 4))
   assert_equal(28, len(xc["boat"].unique()))      
  
  
  