FROM python:3.8.5-alpine

WORKDIR /opt/template_fastapi

ENV PATH "${PATH}:/opt/template_fastapi/sources"
ENV PYTHONPATH "${PYTHONPATH}:/opt/template_fastapi/sources"

EXPOSE 8080/tcp

RUN \
 apk add --no-cache postgresql-libs make && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk --purge del .build-deps

COPY . .

CMD ["python", "./sources/main.py"]
