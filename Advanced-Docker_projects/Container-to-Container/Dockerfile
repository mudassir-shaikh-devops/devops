FROM python
WORKDIR /myapp
COPY ./c2c.py .
RUN pip install mysql-connector-python
RUN pip install cryptography
CMD ["python","c2c.py"]