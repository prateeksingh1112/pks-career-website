from flask import Flask

app = Flask(__name__)

@app.route("/")
def gello_world():
  return "hello pks"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')