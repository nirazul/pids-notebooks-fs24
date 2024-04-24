from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2d"
points = 1
@test_case()
def test_q2d(env):
   alpha = env["Question2d"].alpha
   beta = env["Question2d"].beta

   assert_almost_equal(alpha, 0.002, places=3)
   assert_true(50 < beta < 52)
      
  
  