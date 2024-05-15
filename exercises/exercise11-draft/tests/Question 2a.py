from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2a"
points = 2
@test_case()
def test_q2a(env):
   mean_test_score = env["Question2a"].mean_test_score
   std_test_score = env["Question2a"].std_test_score
   assert_almost_equal(0.97, mean_test_score, 1)
   assert_almost_equal(0.02, std_test_score, 1)
   
      
  