<h1 align="center">Data Science Practice: Assignment 3></h1>

# Description
The app is built for data explorer. The purpose of this app is to perform exploratory data analysis (EDA) on any input datasets so data scientists will be able to obtain a deep understanding of the information in the datasets, as well as identify any issues and limitations. 
This web application is containerized with Docker and Python 3.8.2 is used to run the application. To develop an interactive web application, Streamlit, an open-source python library, is also used and it will only read a CSV file that is provided by the user and perform EDA on it. 
# Authors

**Wenying Wu**

- Student ID: 14007025
- Email: wenying.wu-1@student.uts.edu.au

**Jean Yue Juin Koh** 
- Student ID: 14205823
- Email: jean.y.koh@student.uts.edu.au

# Structure

    ├── api.py             <- python script that will contain the code for calling API endpoints
    ├── currency.py        <- python script that will contain the code for checking if currency code is valid, store results and format final output

    ├── streamlit_app.py   <- main program used for to display the run steamlit app, display local URL and Network URL
    ├── Pipfile            <- not used
    ├── Pipfile.lock       <- not used
    ├── README.md          <- a markdown file containing a description of this project, aurthors details (full name, student id, email), listing of all Python functions and classes and instructions for running your code 
    ├── test_api.py        <- python script for testing code from api.py
    └── test_currency.py   <- python script for testing code from currency.py
# Instructions