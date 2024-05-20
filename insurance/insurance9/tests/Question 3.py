from asserts import *
from otter.test_files import test_case
import random

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_subplots(env):
    mlp = env["Question3"].mlp
    layer_sizes = mlp.hidden_layer_sizes
    act = mlp.activation
    assert_equal((10, 7), layer_sizes)
    assert_equal("tanh", act)