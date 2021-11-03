# To be filled by students
import unittest
import pandas as pd
from src.text import TextColumn

class TestTextColumn(unittest.TestCase):
    def test_col_name(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.col_name = "Country"
        assert mydata.get_name() == "Country"

    # for unique values excluding NA vlaues
    def test_unique_values(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "Spain", "Australia", "Greece"])
        assert mydata.get_unique() == 4

    # for unique values including NA values 
    def test_unique_values_including_na(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "Spain", None, None, "Australia", "Greece"])
        assert mydata.get_unique() == 4

    # for missing values
    def test_missing_values(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "Australia", None, "Australia", None])
        assert mydata.get_missing() == 2

    # for empty values
    def test_empty_values(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "", "Australia", None, "Australia", None, ""])
        assert mydata.get_empty() == 2
    
    # for zero empty values 
    def test_no_empty_values(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "Australia", None, "Australia", None])
        assert mydata.get_empty() == 0

    # for rows with only whitespaces 
    def test_whitespaces(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", " ", "Greece"," ", "Spain", "Australia", " ", None, "Australia", None])
        assert mydata.get_whitespace() == 3

    # for zero number of rows with only whitespaces 
    def test_no_whitespaces(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "Australia", None, "Australia", None])
        assert mydata.get_whitespace() == 0
    
    def test_lowercases(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "spain", "Australia", "australia", "USA"])
        assert mydata.get_lowercase() == 2

    def test_uppercases(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "spain", "Australia", "australia", "USA"])
        assert mydata.get_uppercase() == 2
    
    def test_alphabet(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "spain", "Australia", "australia2", "1", "", " "])
        assert mydata.get_alphabet() == 5

    def test_digit(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "Spain", "spain", "Australia", "australia2", "1", "", " "])
        assert mydata.get_digit() == 1
    
    # for only 1 mode value 
    def test_mode(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "USA", "Spain", "Spain", "Australia", "Australia", "USA"])
        assert mydata.get_mode() == "USA"

    # for multiple mode values 
    def test_multiple_mode(self):
        mydata = TextColumn(col_name=None, serie=None)
        mydata.serie = pd.Series(["USA", "Greece", "USA", "Spain", "Spain", "Spain", "Australia", "Australia", "USA"])
        # displays the first value of mode and this is according to alphabetical order
        assert mydata.get_mode() == "Spain"
