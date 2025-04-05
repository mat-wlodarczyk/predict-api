
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    x = request.args.get('x', default=0, type=float)
    y = request.args.get('y', default=0, type=float)
    sum_of_numbers = x + y

    prediction = 1 if sum_of_numbers > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "x": x,
            "y": y,
            "sum": sum_of_numbers
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
