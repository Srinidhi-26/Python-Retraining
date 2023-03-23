from flask import Flask,request
app = Flask(__name__)
@app.route("/poc1/<x>",methods=["GET"])
def poc1(x):
    return "poc1 "+x
@app.route("/poc2/",methods=["POST"])
def poc2():
    x= request.form["message"]
    print("Hello how are you")
    return "poc2 "+x

@app.route("/getsomenumbers/<x>", methods=['GET'])
def number(x):
    list1 = [7,8,9]
    return list1


@app.route("/getsome/", methods=['GET'])
def num():
    x = request.form["message"]
    dict1 = {"siri":123,"sagi":456 }
    return dict1


if __name__ == "__main__":
    app.run(debug=True)