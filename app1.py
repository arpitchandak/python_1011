from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')

def hlo():
	return render_template("n1.html")

if __name__ == "__main__":
	app.run(port = 9000)
