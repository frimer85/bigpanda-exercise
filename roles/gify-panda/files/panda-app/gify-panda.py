import os.path
from flask import Flask
from flask_autoindex import AutoIndex

pm = __import__("gify-panda")
app=Flask(__name__)
AutoIndex(app, browse_root="/tmp/panda-app/resources")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
