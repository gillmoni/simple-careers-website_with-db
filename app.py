from flask import Flask, render_template
from flask import jsonify

from flask import request
from database import engine
from database import list_jobs_from_db
from database import load_job_from_db
from database import add_application_to_db
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

@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id ):
  data = request.form
  job = load_job_from_db(id)
  
  #store in db
  add_application_to_db(id, data)

  #send an email
  #TODO
  #display an acknowledgement
  return render_template('application_submitted.html',
                         application=data,
                        job=job
                        )


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
