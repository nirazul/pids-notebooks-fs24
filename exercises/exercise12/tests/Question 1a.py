from asserts import *
from otter.test_files import test_case
import numpy as np
OK_FORMAT = False
name = "Question 1a"
points = 1

@test_case()
def test_solution(env):  
    q1 = env["Question1a"]
    assert_equal(q1.grades_tidy.shape, (12,4))


