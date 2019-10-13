# Alpine
FROM surnet/alpine-python-wkhtmltopdf:3.6.4-0.12.4-full

COPY ./requirements.txt /app/requirements.txt
COPY toc.xsl /app/toc.xsl
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]


