from asserts import *
from otter.test_files import test_case
import random

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_subplots(env):
    fsp = env["Question3"].female_survival_prob
    tfsp = 0.69
    r = random.randint(1, 100000)
    assert(tfsp - 0.02 < fsp < tfsp + 0.02 )
    

