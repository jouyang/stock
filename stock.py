from flask import Flask, render_template,request
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method =='POST':
		symbol = request.form['symbol']
		r = requests.get('http://finance.yahoo.com/q?s='+symbol)
		beg = r.text.split('yfs_l84_' + symbol + '">')
		end = beg[1].split('</span>')
		quote1 = end[0]
		return render_template('stock.html',blah=quote1) 
	return render_template('stock.html')

@app.route('/hello')
def hello():
	return render_template('hello.html')


if __name__ == "__main__":
    app.run(debug=True)