from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route("/get_cut_names", methods=["GET"])
def get_cut_names():
    response = jsonify({"cut": util.get_cut_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/get_clarity_categories")
def get_clarity_categories():
    response = jsonify({"clarity": util.get_clarity_categories()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/get_color_categories")
def get_color_categories():
    response = jsonify({"color": util.get_color_categories()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/predict_price", methods=["GET", "POST"])
def predict_price():
    carat = float(request.form["carat"])
    cut = request.form["cut"]
    color = request.form["color"]
    clarity = request.form["clarity"]
    table = float(request.form["table"])
    x = float(request.form["x"])
    y = float(request.form["y"])
    z = float(request.form["z"])
    depth = float(request.form["depth"])
    response = jsonify(
        {
            "estimated_price": util.get_predicted_price(
                carat, cut, color, clarity, table, x, y, z, depth
            )
        }
    )
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    print("Starting server")
    util.load_artifacts()
    app.run(debug=True)
