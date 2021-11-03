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
from datetime_ast3 import DateColumn


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
min = '1/01/1900'
max = ['1/03/2022']



# Create DataFrame using DateColumn()
datecolumn = DateColumn(name,df['Date'])

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
   #     self.assertEqual(datecolumn.get_weekday(), n_weekday)

        # 6. test for datecolumn.get_future()
    #    self.assertEqual(datecolumn.get_future(), get_future)

        # 7. test for datecolumn.get_empty_1900()
     #   self.assertEqual(datecolumn.get_empty_1900()[0], get_empty_1900)

        # 8. test for datecolumn.get_empty_1900()
     #   self.assertEqual(datecolumn.get_empty_1900()[0], get_empty_1900)

        # 9. test for datecolumn.get_max()
      #   self.assertEqual(datecolumn.get_max()[0], max)

   

  
# Print the output.
