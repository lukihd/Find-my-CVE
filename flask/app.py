from flask import (Flask, render_template, request, redirect)
import requests
from flask_bootstrap import Bootstrap
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method=='POST':
        query=request.form['search']
        results=get_datas(query)
        count=len(results)
        return render_template('search.html', results=results, count=count)
    return render_template('base.html')

Bootstrap(app)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)