FROM python:3.12

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY dashboard.py .
COPY dashboard_connection.py .

CMD ["streamlit","run","dashboard.py"]