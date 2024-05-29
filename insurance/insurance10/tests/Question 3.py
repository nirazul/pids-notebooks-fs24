from asserts import *
from otter.test_files import test_case
import random

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_accuracy(env):
    acc = env["Question3"].accuracy
    true_acc = 0.5
    assert_almost_equal(true_acc, acc, 1)