from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2b"
points = 1
@test_case()
def test_q2a(env):
   corr_coeff = env["Question2b"].corr_coeff
   assert_is_instance(corr_coeff, float)
   assert_almost_equal(corr_coeff, 0.85374, places=2)
      
  
  