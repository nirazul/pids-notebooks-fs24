from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 3b"
points = 3
@test_case()
def test_q2a(env):
   X = env["Question3b"].X_nonan
   y = env["Question3b"].y_nonan
   assert_equal((1308, 4), X.shape)
   assert_equal((1308, ), y.shape)
      
  
  
  