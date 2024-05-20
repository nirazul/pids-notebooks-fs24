# +
from otter.test_files import test_case
from asserts import *
import random
import numpy as np 
import scipy
import scipy.stats as stats 

OK_FORMAT = False
name = "Question 1"
points = 1
@test_case()
def test_subplots(env):
    df = env["Question1"].scaled_df
    assert_almost_equal(0, df.mean().mean(), 1)
    assert_almost_equal(1, df.std().mean(), 1)
    


