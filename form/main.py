from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def studant():
	return render_template("studant.html")
	
@app.route("/result",methods=['POST'])
def result():
	if request.method == "POST":
		result = request.format
		print("result")
		print(result)
		return render_template("result.html",result)
	
if __name__== "__main__":
	app.run(host="0.0.0.0",debug=True)