from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2b"
points = 3
@test_case()
def test_q2a(env):
   y_pred = env["Question2b"].y_pred
   r2 = env["Question2b"].r2

   assert_equal(349, y_pred.shape[0])
   assert_true(np.abs(y_pred.mean() -150) <= 10)
   assert_almost_equal(r2, 0.58, places=1)
      
  
  