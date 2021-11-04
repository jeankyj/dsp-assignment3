# To be filled by students
import sys
import os

# add additional path for python to import files in src folder (docker env)
# additional_path = os.path.abspath("..") for windows
# additional_path = os.path.abspath(".") for unix(docker)
additional_path = os.path.abspath("..")
sys.path.insert(0,additional_path)

import pandas as pd
from datetime_ast3 import DateColumn
import unittest


# initialize dataframe of lists.
df = pd.read_csv('test_dataset.csv')
name = 'Date'
n_unique = 8 
n_missing = 1
n_weekend = 1  
n_weekday = 8 
n_future = 1
n_1900 = 1
n_1970 = 1
min = '1900-01-01 00:00:00'
max = '2022-03-01 00:00:00'



# Create DataFrame using DateColumn()
datecolumn = DateColumn(name,pd.to_datetime(df['Date']))

class Testnumeric(unittest.TestCase):
    def test_function(self):

        # 1. test for datecolumn.get_name()
        self.assertEqual(datecolumn.get_name(), name) 

        # 2. test for datecolumn.get_unique()
        self.assertEqual(datecolumn.get_unique(), n_unique)

        # 3. test for datecolumn.get_missing()
        self.assertEqual(datecolumn.get_missing(), n_missing)

        # 4. test for datecolumn.get_weekend()
        self.assertEqual(datecolumn.get_weekend(), n_weekend)

        # 5. test for datecolumn.get_weekday()
        self.assertEqual(datecolumn.get_weekday(), n_weekday)

        # 6. test for datecolumn.get_future()
        self.assertEqual(datecolumn.get_future(), n_future)

        # 7. test for datecolumn.get_empty_1900()
        self.assertEqual(datecolumn.get_empty_1900(), n_1900)

        # 8. test for datecolumn.get_empty_1970()
        self.assertEqual(datecolumn.get_empty_1970(), n_1970)

        # 9. test for datecolumn.get_min()
        self.assertEqual(str(datecolumn.get_min()), min)

        # 10. test for datecolumn.get_max()
        self.assertEqual(str(datecolumn.get_max()), max)

   

  
# Print the output.
