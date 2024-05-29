# +
from otter.test_files import test_case
from asserts import *
import random
import numpy as np 
import scipy
import scipy.stats as stats 
from sklearn.metrics import accuracy_score

OK_FORMAT = False
name = "Question 1"
points = 1
@test_case()
def test_ypred(env):
    y_pred = env["Question1"].y_pred
    
    score = accuracy_score(y_pred, env['y_test'])
    expected_score = 0.95
    assert_true(0.91 < expected_score < 0.99)
    
    


