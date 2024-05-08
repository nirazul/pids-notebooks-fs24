from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 3a"
points = 2
@test_case()
def test_q2a(env):
   r2 = env["Question3a"].r2
   y_pred = env["Question3a"].y_pred
   y = env["Question1a"].y
   assert_true((y - y_pred).abs().mean() < 15)
   assert_true((r2 > 0.99))
      
  
  
  