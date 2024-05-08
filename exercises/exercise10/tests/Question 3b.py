from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 3b"
points = 3
@test_case()
def test_q2a(env):
   X_test = env["Question3b"].X_test
   X_test_scaled = env["Question3b"].X_test_scaled
   r2 = env["Question3b"].r2

   assert_equal((93,10), X_test_scaled.shape)
   assert_almost_equal(1, X_test_scaled.std(axis=1).mean(), 0)
      
  
  
  