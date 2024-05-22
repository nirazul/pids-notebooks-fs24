# +
from otter.test_files import test_case
from asserts import *
import random
import numpy as np 
import scipy
import scipy.stats as stats 

OK_FORMAT = False
name = "Question 4a"
points = 1
@test_case()
def test_subplots(env):
    corr = env["Question4a"].corr
    lb = -0.45
    ub = -0.44
    
    assert(lb < corr < ub)


