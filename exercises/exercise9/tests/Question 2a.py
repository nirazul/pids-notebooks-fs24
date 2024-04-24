from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 2a"
points = 2
@test_case()
def test_q2a(env):
   corr_plot = env["Question2a"].corr_plot
   xlim = corr_plot.get_xlim()
   ylim = corr_plot.get_ylim()
   assert 3000 < xlim[0] < 5000
   assert 20000 < xlim[1] < 23000
   assert 50 < ylim[0] < 70
   assert 120 < ylim[1] < 140
   
      
  