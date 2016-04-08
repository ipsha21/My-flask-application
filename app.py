from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
	if request.method == 'POST':
		if request.form['amswer'] == 'yes':
			return redirect(url_for('password'))
    	return render_template('index.html')

@app.route("/password")
def password():
	return render_template('password.html')

if __name__ == "__main__":
    app.run(debug=True)
