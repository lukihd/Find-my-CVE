from flask import (Flask, render_template, request, redirect)
import os
from pymongo import MongoClient
import requests
app = Flask(__name__)

client = MongoClient("mongodb://root:password@mongodb:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db=client.findmycve

@app.route('/', methods=['GET', 'POST'])
def welcome():
    res=get_all()
    if request.method=='POST' :
        query=request.form.getlist('search')
        results=get_CVE_by_techno(query)
        return render_template('results.html', results=results, query=query)
    return render_template('base.html', res=res)

def get_CVE_by_techno(query):
    results=list()
    for q in query:
        print(q)
        res=list(db.reviews.find({ 'summary': {'$regex': q}}))
        results.append(res)
    return results

def get_all():
    res=list(db.reviews.find())
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)