FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py . 
COPY ./templates/ /app/templates   
COPY ./scripts/ /app/scripts  
CMD ["flask", "run", "--host=0.0.0.0"]
