import os

# Define all folders and files to create
folders = [
    ".github/workflows",
    "backend/routes",
    "backend/services",
    "backend/models",
    "frontend/public",
    "frontend/src/components",
    "frontend/src/pages",
    "data/raw",
    "data/processed",
    "notebooks",
    "tests"
]

files = [
    "README.md",
    ".env",
    "docker-compose.yml",
    ".gitignore",
    "backend/app.py",
    "backend/requirements.txt",
    "backend/Dockerfile",
    "backend/routes/forecast_routes.py",
    ".github/workflows/ci-cd.yml",
    "notebooks/forecasting_baselines.ipynb"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for file_path in files:
    with open(file_path, 'w') as f:
        pass  # Just create the file
    print(f"Created file: {file_path}")

# Optionally add some boilerplate to a few important files
boilerplate = {
    "backend/app.py": '''from flask import Flask
from routes.forecast_routes import forecast_bp

app = Flask(__name__)
app.register_blueprint(forecast_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
''',

    "backend/routes/forecast_routes.py": '''from flask import Blueprint, jsonify

forecast_bp = Blueprint("forecast", __name__)

@forecast_bp.route("/forecast", methods=["GET"])
def forecast():
    return jsonify({"message": "Forecast endpoint is working!"})
''',

    "README.md": "# IntelliSupply\n\nAI-Powered Demand Forecasting & Supply Chain Optimization System.",

    ".gitignore": '''__pycache__/
*.pyc
venv/
.env
mlruns/
node_modules/
.build/
dist/
.DS_Store
''',

    ".github/workflows/ci-cd.yml": '''name: IntelliSupply CI/CD

on:
  push:
    branches: [ main ]

jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt

      - name: Run tests
        run: |
          cd backend
          pytest
'''
}

# Write boilerplate content
for path, content in boilerplate.items():
    with open(path, 'w') as f:
        f.write(content)
    print(f"Added boilerplate to: {path}")
