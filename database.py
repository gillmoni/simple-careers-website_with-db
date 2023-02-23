from sqlalchemy import create_engine
from sqlalchemy import text
import os

# create_engine
URL = os.environ['DB_CONNECTION_STRING']
#Establish connectivity
engine = create_engine(URL,
                       echo=True,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def list_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()

    jobs = []
    for row in result_all:
      # use mapping from here
      # https://stackoverflow.com/questions/1958219/how-to-convert-sqlalchemy-row-object-to-a-python-dict/1958228#1958228
      jobs.append(row._mapping)

    return list(jobs)
