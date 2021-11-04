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
from text import TextColumn

# Initialise dataframe of lists 
df = pd.read_csv('test_dataset.csv')
name = 'Text'
n_unique = 8
n_missing = 1
n_lowercase = 1
n_uppercase = 2
n_alphabet = 7
n_digit = 1
n_mode = 'Apple'

# Create DataFrame using TextColumn()
textcolumn = TextColumn(name, df['Text'])

class TestTextColumn(unittest.TestCase):
    def test_function(self):

        # 1. Test for textcolumn.getname()
        self.assertEqual(textcolumn.get_name(), name)

        # 2. Test for textcolumn.get_unique()
        self.assertEqual(textcolumn.get_unique(), n_unique)

        # 3. Test for textcolumn.get_missing()
        self.assertEqual(textcolumn.get_missing(), n_missing)

        # 4. Test for textcolumn.get_empty()
        textcolumnempty = TextColumn(col_name=None, serie=None)
        textcolumnempty.serie = pd.Series(["Apple", "Banana", "Cherry", "", "", " ", None])
        self.assertEqual(textcolumnempty.get_empty(), 2)

        # 5. Test for textcolumn.get_whitespace()
        textcolumnwhitespace = TextColumn(col_name=None, serie=None)
        textcolumnwhitespace.serie = pd.Series(["Apple", "Banana", "Cherry", "", "", " ", None])
        self.assertEqual(textcolumnwhitespace.get_whitespace(), 1)

        # 6. Test for textcolumn.get_lowercase()
        self.assertEqual(textcolumn.get_lowercase(), n_lowercase)

        # 7. Test for textcolumn.get_uppercase()
        self.assertEqual(textcolumn.get_uppercase(), n_uppercase)

        # 8. Test for textcolumn.get_alphabet()
        self.assertEqual(textcolumn.get_alphabet(), n_alphabet)

        # 9. Test for textcolumn.get_digit()
        self.assertEqual(textcolumn.get_digit(), n_digit)

        # 10. Test for textcolumn.get_mode()
        self.assertEqual(textcolumn.get_mode(), n_mode)
