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
import pandas.testing as pd_testing
from data import Dataset

# Initialize dataframe of lists
df = pd.read_csv('test_dataset.csv')
name = 'test'
n_rows = 10
n_cols = 3
cols_list = ['Date', 'Numeric', 'Text']
cols_dtype_str = "{'Date': dtype('O'), 'Numeric': dtype('float64'), 'Text': dtype('O')}"
n_dup = 1
n_missing = 3
head = df.head(5)
tail = df.tail(5)
numeric_col = ['Numeric']
text_col = ['Date', 'Text']

# Create DataFrame using Dataset()
dataset = Dataset(name,df)

class TestData(unittest.TestCase):
    def test_function(self):

        # 1. test for dataset.get_name()
        self.assertEqual(dataset.get_name(), name) 

        # 2. test for dataset.get_n_rows()
        self.assertEqual(dataset.get_n_rows(), n_rows)

        # 3. test for dataset.get_n_cols()
        self.assertEqual(dataset.get_n_cols(), n_cols)

        # 4. test for dataset.get_cols_list()
        self.assertEqual(dataset.get_cols_list(), cols_list)
        
        # 5. test for dataset.get_cols_dtype()
        self.assertEqual(str(dataset.get_cols_dtype()), cols_dtype_str)
        
        # 6. test for dataset.get_n_duplicates()
        self.assertEqual(dataset.get_n_duplicates(), n_dup)

        # 7. test for dataset.get_n_missing()
        self.assertEqual(dataset.get_n_missing(), n_missing)

        # 8. test for dataset.get_head()
        pd_testing.assert_frame_equal(dataset.get_head(), head)

        # 9. test for dataset.get_tail()
        pd_testing.assert_frame_equal(dataset.get_tail(), tail)

        # 10. test for dataset.get_numeric_columns()
        self.assertEqual(dataset.get_numeric_columns(), numeric_col)
        
        # 11. test for dataset.get_text_columns()
        self.assertEqual(dataset.get_text_columns(), text_col)
        

