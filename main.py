from flask import Flask, render_template, request 
from flask_cors import CORS
from project1.mainp1 import project1  # Importing project1 blueprint
from project2.mainp2 import project2  # Importing project2 blueprint
from contact.main_contact import contact 
import os

app = Flask(__name__)
CORS(app, resources={r"/project1/*": {"origins": "*"}})
CORS(app, resources={r"/project2/*": {"origins": "*"}})
CORS(app, resources={r"/contact/*": {"origins": "*"}})

# Ensure you set a secret key for session management
app.secret_key = os.urandom(24)  # Generates a random secret key for your app

# Register the blueprints for Project 1 and Project 2
app.register_blueprint(project1, url_prefix='/project1')  # All routes under '/project1' will use the project1 blueprint
app.register_blueprint(project2, url_prefix='/project2')  # All routes under '/project2' will use the project2 blueprint
app.register_blueprint(contact, url_prefix='/contact')

# New route for the Home page
@app.route('/home')
def home():
    return render_template('home.html')  # This will render the home.html template

# Route for the Main Landing Page (Portfolio)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
