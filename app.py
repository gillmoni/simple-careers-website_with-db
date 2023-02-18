from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengluru, India',
    'salary':'10,00,000' 
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Pune, India',
    'salary':'20,00,000' 
  },
  {
    'id':32,
    'title':'Backend Engineer',
    'location':'Remote',
    'salary':'30,00,000' 
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)