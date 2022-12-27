FROM python:3.7-slim

RUN mkdir /fastapi

COPY requirements.txt /fastapi

WORKDIR /fastapi

RUN pip3 install -r requirements.txt
RUN pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu117

COPY . /fastapi

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]