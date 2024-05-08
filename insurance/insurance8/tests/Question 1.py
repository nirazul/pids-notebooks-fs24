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
    corr = env["Question1"].corr
    lb = -0.45
    ub = -0.44
    #sassert_is_instance(env["Question1"].bin_dist, scipy.stats._distn_infrastructure.rv_discrete_frozen)
    
    assert(lb < corr < ub)


