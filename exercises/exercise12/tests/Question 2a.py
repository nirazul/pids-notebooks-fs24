# +
from otter.test_files import test_case
from asserts import *
import random

OK_FORMAT = False
name = "Question 2a"
points = 1
@test_case()
def test_subplots(env):
    pl9 = env["Question2a"].probability_lower_9
    tp = 0.72

    assert(tp - 0. < pl9 < tp + 0.01 )
    
# -


