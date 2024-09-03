FROM python:3.12.5

WORKDIR /opt/app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

#CMD [ "python", "/opt/app/main.py" ]
#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
CMD ["tail", "-f", "/dev/null"]
