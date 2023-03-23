from flask import Flask,request
from logic import cal
app = Flask(__name__)

@app.route("/mbr", methods = ["POST"])
def dicto1():
    data=request.json
    result = cal(data)
    return result


if __name__ == "__main__":
    app.run(debug=True)



