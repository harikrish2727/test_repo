from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home_page():
    return "Home page"

@app.route("/ping")
def ping():
    return "Hello I am working"



if __name__=="__main__":
    app.run(debug=True)