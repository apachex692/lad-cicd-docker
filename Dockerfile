# Author: Sakthi Santhosh
# Created on: 26/08/2023
FROM python:3.9.17-alpine3.18 AS build

COPY ./requirements.txt /

RUN pip3 install -q -r /requirements.txt

FROM python:3.9.17-alpine3.18 AS final

WORKDIR /app/

COPY ./ ./
COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

EXPOSE 5000

ENTRYPOINT ["python3", "./app.py"]
