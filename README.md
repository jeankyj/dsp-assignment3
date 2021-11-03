# Data Explorer Web App

**The fastest way to explore data**

## Description
The app is built for data explorer. The purpose of this app is to perform exploratory data analysis (EDA) on any input datasets so data scientists will be able to obtain a deep understanding of the information in the datasets, as well as identify any issues and limitations. 
This web application is containerized with Docker and Python 3.8.2 is used to run the application. To develop an interactive web application, Streamlit, an open-source python library, is also used and it will only read a CSV file that is provided by the user and perform EDA on it. 
The web application is composed of 4 different sections:
- Overall information of the dataset
- Information on each numeric column
- Information on each text column
- Information on each datetime column

## Authors

**Wenying Wu**

- Student ID: 14007025
- Email: wenying.wu-1@student.uts.edu.au

**Jean Yue Juin Koh** 
- Student ID: 14205823
- Email: jean.y.koh@student.uts.edu.au

**Saga Svensson**
- Student ID: 14205823
- Email: saga.e.svensson@student.uts.edu.au

## Structure
The end up structure of the application like

```bash
.
├── app
|   └── streamlit_app.py     <- main program used for to display the run steamlit app, display local URL and Network URL
├── src
|   └── test 
|   |   ├── test_data.py     <- python script for testing code from data.py
|   |   ├── test_datetime.py <- python script for testing code from datetime.py
|   |   ├── test_numeric.py  <- python script for testing code from numeric.py
|   |   └── test_text.py     <- python script for testing code from text.py
|   ├──_init_.py
|   ├── data.py              <- python script that will contain the code for exploring the overall information of the dataset
|   ├── datetime.py          <- python script that will contain the code for exploring the information on each numeric column
|   ├── numeric.py           <- python script that will contain the code for exploring the information on each text column
|   └── text.py              <- python script that will contain the code for exploring the information on each datetime column
├── docker-compose.yml
├── Dockerfile
├── README.md                <- a markdown file containing a description of this project, aurthors details (full name, student id, email), listing of all Python functions and classes and instructions for running your code
└── requirements.txt
```

## Instructions

#### Installation

```bash
pip install streamlit
```

Streamlit can also be installed in a virtual environment on [Windows](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-windows), [Mac](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux), and [Linux](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux).

#### Running the App
+ cd into app
+ run the following

```bash
streamlit run app.py
```

- Build the Docker image from the Dockerfile using the command $ docker build -t dsp_at3:latest .
- Run the built image with 8501 port published and a volume mounted to the current directory /AT3, using the command $ docker run -dit --rm --name at3 -p 8501:8501 -v ~"${PWD}":/AT3 dsp_at3:latest
- Open "localhost:8501" in a browser
