from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>')
def factorial(num):
    try:
        result = math.factorial(num)
        return jsonify({"number": num, "factorial": result})
    except ValueError:
        return jsonify({"error": "Please provide a non-negative integer."}), 400

if __name__ == '__main__':
    app.run() 