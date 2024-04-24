from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2c"
points = 1
@test_case()
def test_q2a(env):
   corr_plot = env["Question2c"].corr_plot
   xlim = corr_plot.get_xlim()
   ylim = corr_plot.get_ylim()
   assert 30 < xlim[0] < 33
   assert 52 < xlim[1] < 54
   assert 50 < ylim[0] < 70
   assert 120 < ylim[1] < 140
   
      
  