from flask import Flask, render_template
from flask import jsonify

from database import engine
from sqlalchemy import text

app = Flask(__name__)

#This is obsolete in DB pull new app
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengluru, India',
  'salary': '10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Pune, India',
  'salary': '20,00,000'
}, {
  'id': 32,
  'title': 'Backend Engineer',
  'location': 'Remote',
  'salary': '30,00,000'
}]


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


@app.route('/')
def hello_world():
  jobs_list = list_jobs_from_db()
  return render_template('home.html', jobs=jobs_list)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
