from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 2c"
points = 3
@test_case()
def test_q2c(env):
    CI = env["Question2c"].CI

    assert_equal(len(CI), 2)
    test = (abs(abs(CI[1] - CI[0]) - 0.054) < 1e-2) or (abs(abs(CI[1] - CI[0]) - 0.193) < 1e-2)
    assert_true(test == True)
    # assert_almost_equal(CI[1] - CI[0], 0.054, places=2)
    test2 = ((np.std(CI) - 0.027) < 1e-2) or ((np.std(CI) - 0.096) < 1e-2)
    assert_true(test2 == True)
    # assert_almost_equal(np.std(CI) , 0.027 , places=2)
    
    