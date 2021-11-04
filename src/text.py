# To be filled by students
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
    #Assuming including null values

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    temp = []
    for i in self.serie:
      if i == '':
        temp.append(i)
    if len(temp) > 0:
      return len(temp)
    return 0

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    temp = []
    for i in self.serie:
      if i == ' ':
        temp.append(i)
    if len(temp) > 0:
      return len(temp)
    return 0

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    return self.serie.str.islower().sum()

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    return self.serie.str.isupper().sum()
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    return self.serie.str.isalpha().sum()

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    return self.serie.str.isnumeric().sum()

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    return self.serie.mode().values[0]


  def get_barchart(self):
    # Display a bar chart showing the number of occurrence for each value 
    """
    Return the generated bar chart for selected column
    """
    chart = alt.Chart(self.serie.to_frame())
    alt.data_transformers.disable_max_rows()
    return chart.mark_bar().encode(
      x = f"{self.col_name}:N",
      y = f"count({self.col_name}):Q"
    )

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    # Assuming includes NA value 
    # Modified to match description - top 20 most frequent values, instead of all
    n = min(20, self.serie.value_counts(dropna=False).shape[0])
    occurrence = self.serie.value_counts(dropna=False).head(n)
    percentage = self.serie.value_counts(dropna=False, normalize=True).head(n)*100
    text_df = pd.DataFrame({'value': occurrence.index, 'occurrence': occurrence, 'percentage': percentage})
    text_df.set_index(pd.Series([i for i in range(n)]),inplace=True)
    return text_df
