FROM python:3.8
LABEL maintainet="Caio F. Gabi"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]