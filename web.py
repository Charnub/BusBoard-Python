from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/busInfo")
def busInfo():
    postcode = request.args.get('postcode')
    return render_template('info.html', postcode=postcode)

if __name__ == "__main__": app.run()