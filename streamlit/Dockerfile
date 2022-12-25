FROM python:3.7-slim

RUN mkdir /streamlit

COPY requirements.txt /streamlit

WORKDIR /streamlit

RUN pip3 install -r requirements.txt

COPY . /streamlit

EXPOSE 8501

CMD ["streamlit", "run", "Homepage.py"]