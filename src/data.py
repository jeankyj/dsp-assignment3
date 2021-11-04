# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class Dataset:
  name: str
  df: pd.DataFrame
  
  def get_name(self):
    """
    Return filename of loaded dataset
    """
    return self.name

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    return self.df.shape[0]

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    return self.df.shape[1]

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    return self.df.columns.tolist()

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """ 
    return self.df.dtypes.to_dict()

  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return self.df.duplicated().sum()

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    return self.df.isnull().sum().sum()

  def get_head(self, n=5):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return self.df.head(n)

  def get_tail(self, n=5):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return self.df.tail(n)

  def get_sample(self, n=5):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return self.df.sample(n)

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
    """
    col_list = self.get_cols_list()
    num_col_list = []
    for i in col_list:
        if self.df[i].dtype != "object" :
            num_col_list.append(i)
    return num_col_list

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    col_list = self.get_cols_list()
    text_col_list = []
    for i in col_list:
        if self.df[i].dtype == "object" :
            text_col_list.append(i)
    return text_col_list

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    # All non-numerical value in pandas dataframe are object,
    # So cannot get list column names of datetime type in
    # Datetime type columns are implemented in main.py
    return None

