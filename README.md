# Data Explorer Web App

**The fastest way to explore data**

## Description
The app is built for data explorer. The purpose of this app is to perform exploratory data analysis (EDA) on any input datasets so data scientists will be able to obtain an initial understanding of the information in the datasets, as well as identify any issues and limitations. 
This web application is designed to run in docker container to avoid any compatibility issue across different OS. Python 3.8.2, streamlit 0.80.0 and pandas 1.3.3 is used to write the application, these versions are choosen to fit the assignment/ design specification and display requirements. To gain a quick understanding of your dataset, just drag and drop the CSV file when the app is running. 
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
|   |   ├── test_dataset.csv <- test dataset
|   |   ├── test_data.py     <- test data.py functions
|   |   ├── test_datetime.py <- test datetime_ast3.py functions
|   |   ├── test_numeric.py  <- test numeric.py functions
|   |   └── test_text.py     <- test text.py functions
|   ├──_init_.py
|   ├── data.py              <- Defines a class for exploring the overall information of the dataset
|   ├── datetime_ast3.py     <- Defines a class for exploring the information on each numeric column
|   ├── numeric.py           <- Defines a class for exploring the information on each text column
|   └── text.py              <- Defines a class for exploring the information on each datetime column
├── docker-compose.yml       <- not used
├── Dockerfile               <- Script for build the required docker container
├── README.md                <- Description and setup instrcution of this project
└── requirements.txt         <- Required packages and versions 
```

## Instructions

### Make sure you have docker available on your computer
#### 1. Clone this repo to your computer say D:/, open bash window at D:/ and type:

```bash
git clone https://github.com/jeankyj/dsp-assignment3.git
```
#### 2. There will be a new folder named dsp-assignment3 appear at D:/, type below in the same bash window:
```bash
cd dsp-assignment3
```
#### 3. Now you are ready to build docker image:
```bash
docker build -t dsp_at3:latest . 
```
##### - 'dsp_at3:latest' is just the name, can be changed but uppercase letter is not allowed
#### 4. Now you are ready to run the docker container:
```bash
docker run -dit --rm --name at3 -p 8501:8501 -v "${PWD}":/AT3 dsp_at3:latest
```
##### - 'at3' is just the name, can be changed
##### - Make sure 'dsp_at3:latest' matches the name you created from the previous step
##### - Leave the bash window open, don't close it
#### 5. It's time to explore your datasest, simply open a browser and type below in the search bar：
```bash
http://localhost:8501
```
##### - Now you can drag and drop any CSV file to the browser and explore!
#### 6. Don't forget to stop the docker container from running after your data exploration, go back to the bash window and type below:
```bash
docker stop at3
```
##### - Make sure 'at3' matches the name you created from step 4

