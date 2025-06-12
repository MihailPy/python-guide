from flask import Flask

app = Flask(__name__)


def add_numbers(a, b):
    """Сложение двух чисел"""
    return a + b


@app.route("/")
def home():
    result = add_numbers(2, 3)
    return f"2 + 3 = {result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
