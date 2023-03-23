from flask import Flask, jsonify, request
from model import task
app = Flask(__name__)
@app.route("/object/",methods=["GET"])
def object():
    a= []
    b = task(1,'hi','message',5)
    a.append(b)
    print(f"value is {a}")
    return jsonify()




if __name__ == "__main__":
    app.run(debug=True)