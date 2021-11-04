# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt


@dataclass
class NumericColumn:
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
    return self.serie.isna().sum()

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """
    temp = []
    for i in self.serie:
      if i == 0:
        temp.append(i)
    if len(temp) > 0:
      return len(temp)
    return 0

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    temp = []
    for i in self.serie:
      if i < 0:
        temp.append(i)
    if len(temp) > 0:
      return len(temp)
    return 0

  def get_mean(self):
    """
    Return the average value for selected column
    """
    return self.serie.mean()

  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    return self.serie.std()
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    return self.serie.min()

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    return self.serie.max()

  def get_median(self):
    """
    Return the median value for selected column
    """
    return self.serie.median()

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    chart = alt.Chart(self.serie.to_frame())
    alt.data_transformers.disable_max_rows()
    return chart.mark_bar().encode(
      x=alt.X(f"{self.col_name}:Q", bin=alt.Bin(step=50)), 
      y="count()"
    )

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    # Assuming includes NA value
    # If the unique value of the serie < 20, return ALL 
    n = min(20, self.serie.value_counts(dropna=False).shape[0])
    occurence = self.serie.value_counts(dropna=False).head(n)
    percentage = self.serie.value_counts(dropna=False, normalize=True).head(n)*100
    d_frame = pd.DataFrame({"value":occurence.index,"occurence":occurence, "percentage":percentage})
    d_frame.set_index(pd.Series([i for i in range(n)]),inplace=True)
    return d_frame
