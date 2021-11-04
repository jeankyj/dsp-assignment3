# To be filled by students
import sys
import os

# add additional path for python to import files in src folder (docker env)
# additional_path = os.path.abspath("..") for windows
# additional_path = os.path.abspath(".") for unix(docker)
additional_path = os.path.abspath("..")
sys.path.insert(0,additional_path)

import unittest
import pandas as pd
import pandas.testing as pd_testing
from numeric import NumericColumn


# initialize dataframe of lists.
df = pd.read_csv('test_dataset.csv')
name = 'Numeric'
n_unique = 8
n_missing = 1
n_zeros = 1  
n_negatives = 1 
mean = 2.0
std = 3
min = -4
max = 6
median = 2



# Create DataFrame using NumericColumn()
numericcolumn = NumericColumn(name,df['Numeric'])

class Testnumeric(unittest.TestCase):
    def test_function(self):

        # 1. test for numericcolumn.get_name()
        self.assertEqual(numericcolumn.get_name(), name) 

        # 2. test for numericcolumn.get_unique()
        self.assertEqual(numericcolumn.get_unique(), n_unique)

        # 3. test for numericcolumn.get_missing()
        self.assertEqual(numericcolumn.get_missing(), n_missing)

        # 4. test for numericcolumn.get_zeros()
        self.assertEqual(numericcolumn.get_zeros(), n_zeros)

        # 5. test for numericcolumn.get_negatives()
        self.assertEqual(numericcolumn.get_negatives(), n_negatives)

        # 6. test for numericcolumn.get_mean()
        self.assertEqual(numericcolumn.get_mean(), mean)

        # 7. test for numericcolumn.get_std()
        self.assertEqual(numericcolumn.get_std(), std)

        # 8. test for numericcolumn.get_min()
        self.assertEqual(numericcolumn.get_min(), min)

        # 9. test for numericcolumn.get_max()
        self.assertEqual(numericcolumn.get_max(), max)

        # 10. test for numericcolumn.get_median()
        self.assertEqual(numericcolumn.get_median(), median)
        

