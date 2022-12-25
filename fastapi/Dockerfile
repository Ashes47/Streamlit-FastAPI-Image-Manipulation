FROM python:3.7
    
# Install torch
RUN pip3 install torch>=1.7
RUN pip3 install torchvision>=0.8.0

RUN mkdir /fastapi

COPY requirements.txt /fastapi

WORKDIR /fastapi

RUN pip3 install -r requirements.txt

COPY . /fastapi

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]