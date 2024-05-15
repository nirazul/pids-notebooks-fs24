from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2c"
points = 2
@test_case()
def test_q2a(env):
   gs = env["Question2c"].grid_search

   assert_true('relu' in gs.best_params_.values()) 
   assert_true((10,) in gs.best_params_.values()) 

      
  
  