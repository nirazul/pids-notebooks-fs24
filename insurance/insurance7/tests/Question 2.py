# +
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 2"
points = 1
@test_case()
def test_q2(env):

    q2 = env["Question2"]
    X = q2.X

    assert_almost_equal(np.mean(np.mean(X, axis = 1)), np.mean(q2.means), places = 2)
    assert_almost_equal(np.mean(np.var(X, axis = 1)), np.mean(q2.vars), places = 5)
   


