from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2b"
points = 1
@test_case()
def test_q2a(env):
   param_grid = env["Question2b"].param_grid

   assert_true("hidden_layer_sizes" in param_grid.keys())
   assert_true("activation" in param_grid.keys())

      
  
  