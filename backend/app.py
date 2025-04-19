from flask import Flask
from routes.forecast_routes import forecast_bp

app = Flask(__name__)
app.register_blueprint(forecast_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
