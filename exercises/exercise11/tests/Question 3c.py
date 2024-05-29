from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 3c"
points = 1
@test_case()
def test_q2a(env):
   X_train = env["Question3c"].X_train
   y_train = env["Question3c"].y_train
   X_val = env["Question3c"].X_val
   y_val = env["Question3c"].y_val
   X_test = env["Question3c"].X_test
   y_test = env["Question3c"].y_test
   
   assert_true(700 < X_train.shape[0] < 800)
   assert_equal(X_train.shape[0], y_train.shape[0])
   
  
   assert_true(200 < X_val.shape[0] < 300)
   assert_equal(X_val.shape[0], y_val.shape[0])
   
   assert_true(200 < X_test.shape[0] < 300)
   assert_equal(X_test.shape[0], y_test.shape[0])
   