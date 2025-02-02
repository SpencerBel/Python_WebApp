from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Create Flask app instance
app = Flask(__name__)
# Enable CORS for 'app'
CORS(app)

# Set DB URI to DB hosted on Neon
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://webapp-db_owner:dF15ZNjevYfP@ep-lucky-sound-a5hjaogd-pooler.us-east-2.aws.neon.tech/webapp-db?sslmode=require"
# Disable tracking (good practice)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Initialize SQLAlchemy ORM (object-relational mapping)
db = SQLAlchemy(app)

# Route decorator
@app.route('/')
def hello():
    return "Test API"