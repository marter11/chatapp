from flask import Flask, render_template
app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Views
from . import login, register
