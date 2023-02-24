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

def load_job_from_db(val):
  with engine.connect() as conn:
    stmt = text(f"SELECT * FROM jobs WHERE id = {val}")
    result = conn.execute(stmt)
    rows = result.all()
    
    if len(rows) == 0:
      return None
    else:
      # _mapping since sqlalchemy2.0
      return rows[0]._mapping

def add_application_to_db(job_id, data):
   with engine.connect() as conn:
     stmt = text(f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) \
            VALUES ( {job_id}, \"{data['full_name']}\", \"{data['email']}\", \"{data['linkedin_url']}\", \"{data['education']}\", \"{data['work_experience']}\", \"{data['resume_url']}\")")
     result = conn.execute(stmt)
  