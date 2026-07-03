FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install \
 --trusted-host pypi.org \
 --trusted-host file.pythonhosted.org \
 -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
