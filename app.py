from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title" : "Data Analyst",
    "location" : "Bengaluru, India",
    "salary" : "Rs. 10,00,000"
  },
  {
    "id": 2,
    "title" : "Backend Engineer",
    "location" : "Delhi, India",
    "salary" : "Rs. 15,00,000"
  },
  {
    "id": 3,
    "title" : "Data Engineer",
    "location" : "Pune, India"
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Prateeks')

@app.route("/jobs")
def get_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')