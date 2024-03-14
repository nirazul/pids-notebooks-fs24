from otter.test_files import test_case
from asserts import *
import pandas as pd 

OK_FORMAT = False
name = "Question 2d"
points = 1
@test_case()
def test_lowage_rank(env):
  df_rank = env['Question2d'].df_rank
  df_wage = env['Question2d'].df_wage
  df_employed = env['Question2d'].df_employed

  assert_equal(type(df_rank), pd.core.series.Series)
  assert_equal(df_rank.name, 'Rank')
  assert_equal(type(df_wage), pd.core.series.Series)
  assert_equal(df_wage.name, 'Low_wage_jobs')
  assert_equal(type(df_wage), pd.core.series.Series)
  assert_equal(df_employed.name, 'Employed')

## test ##
