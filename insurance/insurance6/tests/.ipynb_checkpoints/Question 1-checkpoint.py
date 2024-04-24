# +
from otter.test_files import test_case
from asserts import *
import random

OK_FORMAT = False
name = "Question 1"
points = 1
@test_case()
def test_subplots(env):
    pl9 = env["Question1"].probability_lower_9
    tp = 0.72

    assert(tp - 0.1 < pl9 < tp + 0.01 )
    
# -


