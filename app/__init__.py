from flask import Flask


app = Flask(__name__)
app._static_folder = ""


from app import routes