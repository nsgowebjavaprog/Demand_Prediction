from flask import Flask
from routes.forecast_routes import forecast_blueprint

# Initialize the Flask app
app = Flask(__name__)

# Register the blueprint for forecast routes
app.register_blueprint(forecast_blueprint, url_prefix='/forecast')

# Main route to check if the app is running
@app.route('/')
def index():
    return "Welcome to the Demand Prediction API!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
