
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1e"
points = 2
@test_case()
def test_clt_fit(env):
  answer_1e = env["Question1e"].answer_1e
  assert_equal(answer_1e, 3)
