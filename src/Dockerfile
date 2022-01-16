FROM python:latest
WORKDIR .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
CMD ["uvicorn","server:app","--host","0.0.0.0"]

