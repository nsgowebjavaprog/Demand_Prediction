from flask import Flask
from routes.forecast_routes import forecast_blueprint

app = Flask(__name__)

# Register blueprints or routes
app.register_blueprint(forecast_blueprint, url_prefix='/forecast')

if __name__ == '__main__':
    app.run(debug=True, port=8080)