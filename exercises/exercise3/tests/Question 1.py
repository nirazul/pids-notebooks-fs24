from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1"
points = 1
@test_case()
def test_unemployed_plot(df, env):
  assert (len(df.columns)== env['pd'].options.display.max_columns) \
    or (env['pd'].options.display.max_columns == None) \
    or (env['pd'].options.display.max_columns >= 21
)

