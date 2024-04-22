from flask import Flask
from VirtualPainter import VirtualPainter

app = Flask(__name__)
app.register_blueprint(VirtualPainter, url_prefix="")

if __name__ == "__main__":
    app.run(debug=True)
