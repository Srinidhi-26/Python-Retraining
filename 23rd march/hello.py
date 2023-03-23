from flask import Flask
app = Flask(__name__)

@app.route("/hello/",methods =['POST'])
def hello_world():
    print('hi')
    return "Web application using flask!"

app.run(debug=True)
