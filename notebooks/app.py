from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route("/")
def home():
    return "Witaj w moim API!"

@app.route("/mojastrona")
def my_page():
    return "To jest moja strona!"

@app.route("/hello")
def hello():
    name = request.args.get("name")
    return f"Hello {name}!" if name else "Hello!"

@app.route("/api/v1.0/predict")
def predict():
    try:
        num1 = float(request.args["num1"])
        num2 = float(request.args["num2"])
    except KeyError:
        abort(400, description="Brakuje parametru num1 lub num2")
    except ValueError:
        abort(400, description="num1 i num2 muszą być liczbami")

    prediction = 1 if (num1 + num2) > 5.8 else 0
    return jsonify(prediction=prediction,
                   features={"num1": num1, "num2": num2})

if __name__ == "__main__":
    app.run(debug=True)
