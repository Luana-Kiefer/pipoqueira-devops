import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pipoqueira DevOps</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background-color: #1e1e1e;
            padding: 2rem 3rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            border: 1px solid #333;
        }
        h1 {
            color: #ffb703;
            margin-bottom: 0.5rem;
        }
        .badge {
            display: inline-block;
            background-color: #2a9d8f;
            color: #fff;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🍿 Pipoqueira DevOps</h1>
        <p>Aplicação implantada via pipeline automatizado CI/CD + DevSecOps.</p>
        <span class="badge">Status: Online • AWS EC2 + Docker</span>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE), 200

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "pipoqueira-devops"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)  # nosec B104