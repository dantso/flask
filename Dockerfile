FROM python:3
WORKDIR .
ADD . .

RUN pip install -r requirements.txt

ENV AWS_ACCESS_KEY_ID='[your access key id]'
ENV AWS_SECRET_ACCESS_KEY='[your secret]'

ENTRYPOINT ["python", "./billing.py"]
