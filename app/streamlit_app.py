import sys
import os
from typing import Text
import streamlit as st
import pandas as pd

# add additional path for python to import files in src folder (docker env)
# additional_path = os.path.abspath("..") + "\\src" for windows
# additional_path = os.path.abspath(".") + "/src" for unix(docker)
additional_path = os.path.abspath(".") + "/src"
sys.path.insert(0,additional_path)

from data import Dataset
from numeric import NumericColumn
from text import TextColumn


def main():
    st.title("Data Explorer Tool")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Below stuffs show only after file is uploaded
    if uploaded_file:
        name = uploaded_file.name
        df = pd.read_csv(uploaded_file)
        dataset = Dataset(name, df)

        # 1st part starts
        st.header("1. Overall Information")
        st.write(f"__Name of Table__: {dataset.get_name()}")
        st.write(f"__Number of Rows__: {dataset.get_n_rows()}")
        st.write(f"__Number of Columns__: {dataset.get_n_cols()}")
        st.write(f"__Number of Duplicated Rows__: {dataset.get_n_duplicates()}")
        st.write(f"__Number of Rows with Missing Values__: {dataset.get_n_missing()}")
        st.write("__List of Columns__:")
        st.write(f"{str(', '.join(dataset.get_cols_list()))}")
        st.write("__Type of Columns__:")
        dtype_dict = dataset.get_cols_dtype()
        dtype_index = []
        dtype_value = {"type":[]}
        for i in dtype_dict:
            dtype_index.append(i) 
            dtype_value["type"].append(str(dtype_dict[i]))
        dtype_display = pd.DataFrame(dtype_value, index=dtype_index)
        st.write(dtype_display)


        filter_num = st.slider('Select the number of rows to be displayed', 5, 50, 5)
        st.write("__Top Rows of Table__")
        st.dataframe(dataset.get_head(filter_num))
        st.write("__Bottom Rows of Table__")
        st.dataframe(dataset.get_tail(filter_num))
        st.write("__Random Sample Rows of Table__")
        st.dataframe(dataset.get_sample(filter_num))

        # to be used in part 4, date_cols is a list
        # selections are columns with object(non-numerical) data type by assumption
        date_cols = st.multiselect("Which columns do you want to convert to dates", dataset.get_text_columns())
        # 1st part end

        # 2nd part starts
        st.header("2. Numeric Column Information")
        num_cols = dataset.get_numeric_columns()
            
        for i in range(len(num_cols)):    
            col = NumericColumn(num_cols[i],df[num_cols[i]])
            st.subheader(f"2.{i} Field Name: *{num_cols[i]}*") # * for Italic

            num_index = ["Number of Unique Values", "Number of Rows With Missing Values",
                                "Number of Rows with 0", "Number of Rows with Negative Value",
                                "Average Value", "Standard Deviation Value", "Minimum Value",
                                "Maximum Value", "Median Value"]
            num_stat = {"value":[col.get_unique(), col.get_missing(), col.get_zeros(), 
                                col.get_negatives(), col.get_mean(), col.get_std(),
                                col.get_min(), col.get_max(), col.get_median()]}
            num_display = pd.DataFrame(num_stat, index=num_index)
            st.write(num_display)
            
            st.write("__Histogram__")
            st.altair_chart(col.get_histogram())

            st.write("__Most Frequent Values__")
            st.dataframe(col.get_frequent())
        # 2nd part end

        # 3rd part starts
        st.header("3. Text Column Information") #This header not in Assignment Brief 
        text_cols = dataset.get_text_columns()

        for i in range(len(text_cols)):
            col = TextColumn(text_cols[i], df[text_cols[i]])
            st.subheader(f"3.{i} Field Name: *{text_cols[i]}*")

            text_index = ["Number of Unique Values", "Number of Rows with Missing Values",
                                "Number of Empty Rows", "Number of Rows with Only Whitespace",
                                "Number of Rows with Only Lowercases", "Number of Rows with Only Uppercases",
                                "Number of Rows with Only Alphabet", "Number of Rows with Only Digits",
                                "Mode Value"]
            text_stat = {"value":[col.get_name(), col.get_unique(), col.get_missing(),
                                col.get_empty(), col.get_whitespace(), col.get_lowercase(),
                                col.get_uppercase(), col.get_digit(), col.get_mode()]}
            text_display = pd.DataFrame(text_stat, index=text_index)
            st.write(text_display)

            st.write("__Bar Chart__")
            st.altair_chart(col.get_barchart())

            st.write("__Most Frequent Values__")
            st.dataframe(col.get_frequent())
        # 3rd part ends 
        
        

main()
