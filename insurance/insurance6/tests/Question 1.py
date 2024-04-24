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
    samples = env["Question1"].samples
    m = np.mean(samples)
    lb = 0.8
    ub = 1.2
    #sassert_is_instance(env["Question1"].bin_dist, scipy.stats._distn_infrastructure.rv_discrete_frozen)
    assert_true(len(samples) == 1000)
    assert(lb < m < ub)


