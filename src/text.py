# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt


@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series
  
  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return self.serie.nunique()

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna.sum()

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    return None

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    return self.serie.str.isspace()

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    return self.serie.str.islower()

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    return self.serie.str.isupper()
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    return self.serie.str.isalpha()

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    return self.serie.str.isnumeric()

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    return self.serie.mode()


  def get_barchart(self):
    # Display a bar chart showing the number of occurrence for each value 
    """
    Return the generated bar chart for selected column
    """
    df = self.serie.to_frame()
    chart = alt.Chart(df)
    alt.data_transformers.disable_max_rows()
    chart.mark_bar().encode(
      x = {self.col_name},
      y = 'count()'
    )

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    # Assuming includes NA value? 
    occurrence = self.serie.value_counts(dropna=True)
    percentage = self.serie.value_counts(dropna=True, normalize=True)
    text_df = pd.DataFrame({'value': occurrence.index, 'occurrence': occurrence, 'percentage': percentage})
    return text_df