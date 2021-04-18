import pytest
import hashlib
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model
from testbook import testbook
    

@pytest.fixture(scope='module')
def tb():
  with testbook('hw2.ipynb', execute=True) as tb:
    yield tb

    
def test_pass(tb):
    pass
    
# def test_step_1(tb):
  
#   try:
#     complete = None
#     complete = tb.ref('STEP_1_COMPLETE')
#   except:
#     # STEP_1_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 1: not complete.'
    
#   try:
#     df = str(tb.ref('df')).encode('utf-8')
#   except:
#     assert False, 'STEP 1: df does not exist.'
    
#   assert hashlib.md5(df).hexdigest() == 'affd27e4915d193ed6aaa90b650cde78', \
#     'STEP 1: The dataframe df does not match the auto.csv file with NaN values removed. Be sure you are importing the correct file, ' \
#     'and that you are removing the NaN values (indicated as "?" in auto.csv).'
   
    
# def test_step_2(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_2_COMPLETE')
#   except:
#     # STEP_2_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 2: not complete.'
    
    
# def test_step_3(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_3_COMPLETE')
#   except:
#     # STEP_3_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 3: not complete.'
    
#   try:
#     beta1guess = tb.ref('beta1guess')
#   except:
#     assert False, 'STEP 3: beta1guess does not exist'
    
#   tb.inject("assert isinstance(beta1guess, float), 'STEP 3: beta1guess is a ' + str(type(beta1guess)) + '. It should be a float.'")

    
# def test_step_4(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_4_COMPLETE')
#   except:
#     # STEP_4_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 4: not complete.'
  
#   try:
#     beta1bracket = tb.ref('beta1bracket')
#   except:
#     assert False, 'STEP 4: beta1bracket does not exist'
  
#   tb.inject("assert isinstance(beta1bracket, np.ndarray), 'STEP 4: beta1bracket is a ' + str(type(beta1bracket)) + '. It should be a np.ndarray.'")
#   tb.inject(
#     """
#     assert min(beta1bracket[0],beta1bracket[-1]) <= beta1guess <= max(beta1bracket[0],beta1bracket[-1]), \
#       'STEP 4: beta1bracket does not bracket the beta1guess. beta1bracket[0] is ' + str(beta1bracket[0]) + '. beta1bracket[-1] is ' + str(beta1bracket[1]) + \
#       '. beta1guess ' + str(beta1guess) + ' should be between beta1bracket[0] and beta1bracket[-1].'
#     """
#   )

    
# def test_step_5(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_5_COMPLETE')
#   except:
#     # STEP_5_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 5: not complete.'  
    
#   try:
#     beta1bracket = tb.ref('rss1d')
#   except:
#     assert False, 'STEP 5: rss1d does not exist'
    
#   tb.inject(
#     """
#     try:
#       temp_rssbetas = rss1d(40., 0.1, df.horsepower, df.mpg)
#     except Exception as e:
#       if hasattr(e, 'message'):
#         assert False, 'STEP 9: rss1d returns an error when called with rss1d(40., 0.1, df.horsepower, df.mpg). The error returned is "' + e.message + '".'
#       else:
#         assert False, 'STEP 9: rss1d returns an error when called with rss1d(40., 0.1, df.horsepower, df.mpg). The error returned is "' + str(e) + '".'
#     """
#   )
#   tb.inject("assert isinstance(temp_rssbetas, float), 'STEP 9: rss1d(40., 0.1, df.horsepower, df.mpg) returns ' + str(type(temp_rssbetas)) + '. It should return a float.'")
#   tb.inject("assert np.isclose(temp_rssbetas, 333689.2200000003), 'STEP 9: rss1d(40., 0.1, df.horsepower, df.mpg) returns the wrong value. Returned ' + temp_rssbetas + '. Should return 333689.2200000003.'")
#   tb.inject("temp_rssbetas = rss1d(40., -0.1, df.horsepower, df.mpg)")
#   tb.inject("assert np.isclose(temp_rssbetas, 25944.739999999998), 'STEP 9: rss1d(40., -0.1, df.horsepower, df.mpg) returns the wrong value. Returned ' + temp_rssbetas + '. Should return 25944.739999999998.'")
    
    
# def test_step_6(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_6_COMPLETE')
#   except:
#     # STEP_6_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 6: not complete.' 
    
#   try:
#     beta1min = tb.ref('beta1min')
#   except:
#     assert False, 'STEP 6: beta1min does not exist'
#   assert abs(-0.158 - beta1min) < 0.01, 'STEP 6: Your beta1min value is not within 0.01 of the target beta1 minimum value. Try improving your beta1guess or reducing the distance between values in your beta1bracket array.' 
    
    
# def test_step_7(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_7_COMPLETE')
#   except:
#     # STEP_7_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 7: not complete.'    
    
    
# def test_step_8(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_8_COMPLETE')
#   except:
#     # STEP_8_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 8: not complete.'    
    
    
# def test_step_9(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_9_COMPLETE')
#   except:
#     # STEP_9_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 9: not complete.' 
    
#   tb.inject(
#     """
#     try:
#       betas = computeBetas(df.horsepower, df.mpg)
#     except Exception as e:
#       if hasattr(e, 'message'):
#         assert False, 'STEP 9: computeBetas does not exist or returns an error. The error returned is "' + e.message + '".'
#       else:
#         assert False, 'STEP 9: computeBetas does not exist or returns an error. The error returned is "' + str(e) + '".'
#     """
#   )
#   tb.inject("assert isinstance(betas, np.ndarray), 'STEP 9: computeBetas returns ' + str(type(betas)) + '. It should return a numpy.ndarray.'")
#   tb.inject("assert betas.shape == (2,), 'STEP 9: computeBetas returns an array of the wrong shape. Verify that it returns a 1d array with 2 elements (2,).'")
#   tb.inject("assert np.isclose(betas[0], 39.935861), 'STEP 9: computeBetas function is incorrect. Check beta[0].'")
#   tb.inject("assert np.isclose(betas[1], -0.157845), 'STEP 9: computeBetas function is incorrect. Check beta[1].'")
    
    
# def test_step_10(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_10_COMPLETE')
#   except:
#     # STEP_10_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 10: not complete.'    
    
    
# def test_step_11(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_11_COMPLETE')
#   except:
#     # STEP_11_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 11: not complete.'    
    
    
# def test_step_12(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_12_COMPLETE')
#   except:
#     # STEP_12_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 12: not complete.'    
    
    
# def test_step_13(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_13_COMPLETE')
#   except:
#     # STEP_13_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 13: not complete.'    
  
#   tb.inject(
#     """
#     if 'mpg_hp_model' not in locals():
#       assert False, 'mpg_hp_model does not exist. Be sure to declare mpg_hp_model as a sklearn Linear Regression model.'
#     """
#   )
#   tb.inject("assert isinstance(mpg_hp_model, linear_model._base.LinearRegression), 'mpg_hp_model is not a Linear Regression model. Ensure that you are using the sklearn package.'")
    
#   try:
#     beta0 = tb.ref('beta0')
#   except:
#     assert False, 'STEP 13: beta0 does not exist.'
#   assert np.isclose(beta0, 39.93586102117047), 'STEP 13: The value for beta0 is incorrect'
    
#   try:
#     beta1 = tb.ref('beta1')
#   except:
#     assert False, 'STEP 13: beta1 does not exist.'
#   assert np.isclose(beta1[0], -0.15784473335365365), 'STEP 13: The value for beta1 is incorrect'

#   try:
#     r2 = tb.ref('r2')
#   except:
#     assert False, 'STEP 13: r2 does not exist.'
#   assert np.isclose(r2, 0.6059482578894348), 'STEP 13: The value for r2 is incorrect'

#   try:
#     mse = tb.ref('mse')
#   except:
#     assert False, 'STEP 13: mse does not exist.'
#   assert np.isclose(mse, 23.943662938603108), 'STEP 13: The value for mse is incorrect'
  
    
# def test_step_14(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_14_COMPLETE')
#   except:
#     # STEP_14_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 14: not complete.'    
    
    
# def test_step_15(tb):
#   try:
#     complete = None
#     complete = tb.ref('STEP_15_COMPLETE')
#   except:
#     # STEP_15_COMPLETE constant has been removed, set to true
#     complete = True
#   finally:
#     assert complete, 'STEP 15: not complete.' 
  
