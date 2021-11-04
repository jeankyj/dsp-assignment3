# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt

@dataclass
class DateColumn:
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

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    weekend_list = []
    weekday = self.serie.dt.weekday
    for i in weekday:
      if i >= 5:
        weekend_list.append(i)
    return len(weekend_list)

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    weekday_list = []
    weekday = self.serie.dt.weekday
    for i in weekday:
      if i < 5:
        weekday_list.append(i)
    return len(weekday_list)
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    future_list = []
    for i in self.serie:
      if i > pd.Timestamp('now'):
        future_list.append(i)
    return len(future_list)

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    specific_date_list = []
    for i in self.serie:
      if i == pd.Timestamp('1900-01-01'):
        specific_date_list.append(i)
    return len(specific_date_list)

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    specific_date_list = []
    for i in self.serie:
      if i == pd.Timestamp('1970-01-01'):
        specific_date_list.append(i)
    return len(specific_date_list)

  def get_min(self):
    """
    Return the minimum date
    """
    return self.serie.min()

  def get_max(self):
    """
    Return the maximum date 
    """
    return self.serie.max()

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    chart = alt.Chart(self.serie.to_frame())
    alt.data_transformers.disable_max_rows()
    return chart.mark_bar().encode(
      x=alt.X(f"{self.col_name}:T"), 
      y="count()"
    )

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    # Assuming includes NA value
    # If the unique value of the serie < 20, return ALL 
    n = min(20, self.serie.value_counts(dropna=False).shape[0])
    count = self.serie.value_counts(dropna=False).head(n)
    percent = self.serie.value_counts(dropna=False, normalize=True).head(n)*100
    d_frame = pd.DataFrame({"value":count.index,"occurence":count, "percentage":percent})
    d_frame.set_index(pd.Series([i for i in range(n)]),inplace=True)
    return d_frame
