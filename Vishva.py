from flask import Flask, render_template_string
import random

app = Flask(__name__)

filename = 'Vishva.txt'
try:
    with open(filename, 'r', encoding='utf-8') as f:
        names = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    names = ["Файл не найден"]

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Генерация Имён</title>
    <meta http-equiv="refresh" content="8">
    <style>
        body {
            background-color: #fffde7;
        }
    </style>
</head>
<body>
    <h1>{{ name }}</h1>
</body>
</html>
"""

@app.route("/")
def index():
    name = random.choice(names)
    return render_template_string(TEMPLATE, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

