from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 6"
points = 1
@test_case()
def cat_totals(env):
  cat_totals = env["Question6"].cat_totals
  assert_equal(len(cat_totals),16)
  assert_equal(cat_totals["Interdisciplinary"],12296)
  assert_equal(cat_totals["Engineering"],537583)