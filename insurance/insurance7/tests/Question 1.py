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
    q1 = env["Question1"]
    samples = q1.samples
    
    assert_equal((q1.m, q1.N), samples.shape )
    assert_almost_equal(4, np.mean(np.var(samples, axis=1)), places = 1)
    

