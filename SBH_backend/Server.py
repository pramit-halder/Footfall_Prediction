from flask import Flask, request
from flask_cors import CORS, cross_origin
from model_ew import m_ew
from model_ar import m_ar
from model_sar import m_sar
app = Flask("__name__")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/model1", methods=["POST"])
@cross_origin()
def m_1():
    r = request.json["x"]
    r1 = int(r)
    r2 = m_ar(r1)
    return r2


@app.route("/model2", methods=["POST"])
@cross_origin()
def m2():
    q = request.json["x"]
    q1 = int(q)
    q2 = m_sar(q1)
    return q2


@app.route("/model3", methods=["POST"])
@cross_origin()
def m3():
    p = request.json["x"]
    p1 = int(p)
    p2 = m_ew(p1)
    return p2


if __name__ == "__main__":
    print("server running")
    app.run(debug=True)
