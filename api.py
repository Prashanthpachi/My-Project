from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('welcome.html')

@app.route("/login", methods = ['POST'])
def login():
	if(request.form["password"] == "pachi" and request.form["username"] == "Prashanth"):
		print("login succesfull. Redirecting to products page")
		return redirect(url_for('product_page'))

	else:
		return render_template('error.html')

@app.route("/products")
def product_page():
	return render_template('products.html')


if(__name__ == "__main__"):
	app.run()

