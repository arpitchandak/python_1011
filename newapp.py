from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def hello():
	return render_template("form.html")

@app.route('/form',methods=["post"])
def fb():
	enroll = request.form["enrollment"]
	name = request.form["name"]
	mail = request.form["mail"]
	print(enroll , name, mail)
	return render_template("new.html", enroll=enroll , name=name , mail=mail)
	
if __name__ == '__main__':
	app.run(port=6050,debug = 2)
