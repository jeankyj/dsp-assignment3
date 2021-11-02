# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import seaborn as sns


@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series

  def get_name(self):
    """
    data = {'subtitle':[......]}
    df= pd.DataFrame(data)
    df
    
    for col in df.columns
    print(col)
   
    """
    return None

  def get_unique(self):
    """
   a_list = [?, ?, ?, ?, ?]
a_set = set(a_list)
number_of_unique_values = len(a_set)
print(number_of_unique_values)
    """
    return None

  def get_missing(self):
    """
    data = sns.load_dataset("data")
    data.isna()
    data.isna().sum()
    data.isna().
         sum().
         reset_index(name="n").
         plot.bar(x='index', y='n', rot=45)
    """
    return None

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    return None

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    return None
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    return None

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    return None

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    return None

  def get_min(self):
    """
    Return the minimum date
    """
    return None

  def get_max(self):
    """
    Return the maximum date 
    """
    return None

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    return None
