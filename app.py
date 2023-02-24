from flask import Flask, render_template
from flask import jsonify

from database import engine
from database import list_jobs_from_db
from database import load_job_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  jobs_list = list_jobs_from_db()
  return render_template('home.html', jobs=jobs_list)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)

  if not job:
    return "Not Found", 404
  
  return render_template('jobpage.html', job=job)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
