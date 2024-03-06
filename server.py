from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "My server is on."

@app.route("/info", methods=["GET"])
def server_info():
    out_string = "BME 547 Class Demo Server<br>"
    out_string += "Written by David Ward"
    return out_string

@app.route("/HDL", methods=["POST"])
def HDL_analysis():
    """
      in_json = {"HDL_value": <int>}
    """
    from blood_calculator import analyse_HDL
    in_json = request.get_json()
    HDL_value = in_json["HDL_value"]
    answer = analyse_HDL(HDL_value)
    print("For input value of {}".format(HDL_value))
    print(" the result is {}".format(answer))
    return jsonify(answer), 200


@app.route("/HDL_in/<HDL_value>/<patient>", methods=["GET"])
def HDL_analysis_2(HDL_value, patient):
    from blood_calculator import analyse_HDL
    value = int(HDL_value)
    answer = analyse_HDL(value)
    ans = "{} is {}".format(patient, answer)
    return ans




if __name__ == '__main__':
    app.run(port=5003)
    print("Server is off")
