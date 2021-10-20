FROM python:3.8.2

WORKDIR /AT3

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app/streamlit_app.py"]