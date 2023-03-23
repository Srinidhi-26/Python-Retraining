from flask import Flask, request, app
app = Flask(__name__)

@app.route("/il",methods=['POST'])
def takeInputViaBody():
    print(request.json)
    data=request.json
    print(data['length'])
    dict1 ={'siri':3, 'sagar':4}
    return dict1


if __name__ == "__main__":
    app.run(debug=True)
