from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "key_to_text"

from app import routes
