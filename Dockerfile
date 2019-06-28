FROM library/python

RUN pip install flask

ADD app.py /app.py
CMD python /app.py

EXPOSE 5000
