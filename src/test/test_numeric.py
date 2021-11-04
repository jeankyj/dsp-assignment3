# To be filled by students
import sys
import os

# Add additional path for python to import files in src folder (docker env)
# Additional_path = os.path.abspath("..") for windows
# Additional_path = os.path.abspath(".") for unix(docker)
additional_path = os.path.abspath("..")
sys.path.insert(0,additional_path)

import unittest
import pandas as pd
from numeric import NumericColumn

# Initialize dataframe of lists
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

class TestNumericColumn(unittest.TestCase):
    def test_function(self):

        # 1. Test for numericcolumn.get_name()
        self.assertEqual(numericcolumn.get_name(), name) 

        # 2. Test for numericcolumn.get_unique()
        self.assertEqual(numericcolumn.get_unique(), n_unique)

        # 3. Test for numericcolumn.get_missing()
        self.assertEqual(numericcolumn.get_missing(), n_missing)

        # 4. Test for numericcolumn.get_zeros()
        self.assertEqual(numericcolumn.get_zeros(), n_zeros)

        # 5. Test for numericcolumn.get_negatives()
        self.assertEqual(numericcolumn.get_negatives(), n_negatives)

        # 6. Test for numericcolumn.get_mean()
        self.assertEqual(numericcolumn.get_mean(), mean)

        # 7. Test for numericcolumn.get_std()
        self.assertEqual(numericcolumn.get_std(), std)

        # 8. Test for numericcolumn.get_min()
        self.assertEqual(numericcolumn.get_min(), min)

        # 9. Test for numericcolumn.get_max()
        self.assertEqual(numericcolumn.get_max(), max)

        # 10. Test for numericcolumn.get_median()
        self.assertEqual(numericcolumn.get_median(), median)
        

