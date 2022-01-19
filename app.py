from flask import Flask, render_template

app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/bot")
def login():
    return render_template('bot.html')

@app.route("/test")
def test():
    return render_template('test.html')


 
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)
