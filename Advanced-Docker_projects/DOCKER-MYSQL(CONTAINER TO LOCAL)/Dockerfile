FROM python
WORKDIR /myapp
COPY ./database_connect.py .
RUN pip install mysql-connector-python
CMD ["python","database_connect.py"]