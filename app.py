# flask_web/app.py
# https://runnable.com/docker/python/dockerize-your-flask-application

from flask import Flask
app = Flask(__name__)

@app.route("/")
def health():
    return "200"

@app.route("/predict", methods=['GET','POST'])
def predict():
    return "Prediction result [0.1,0.35,0.4]"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
