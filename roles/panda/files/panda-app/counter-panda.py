from flask import Flask, request

postCount=0
app=Flask(__name__)

@app.before_request
def before_request():
    if request.method == "POST":
        global postCount
        postCount += 1


@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        global postCount
        return "Number of POST requests: " + str(postCount) + "\n"
    else:
        return "\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
