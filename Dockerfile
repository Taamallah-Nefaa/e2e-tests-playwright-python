FROM mcr.microsoft.com/playwright/python:v1.30.0-focal

WORKDIR /app

COPY features /app/features
#COPY utilities /app/utilities

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && pip install behavex

CMD ["behavex"]