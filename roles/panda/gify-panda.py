import os.path
from flask import Flask, send_from_directory
from flask.ext.autoindex import AutoIndex

app=Flask(__name__)
AutoIndex(app, browse_root=os.path.curdir+"/Sample-Files")

if __name__ == "__main__":
    app.run()
