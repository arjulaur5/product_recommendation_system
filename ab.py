from flask import Flask, redirect, url_for, request
import flask
app = flask.Flask(__name__, template_folder='templates')
import sys, json
import pickle,gzip
import pandas as pd
import numpy as np
from collections import Counter
import pyrebase 

app = Flask(__name__)


'''config = {
	"apiKey": "AIzaSyC8Rz0y8TZLBkyiHdeWfCaLnPCTMvMkOgc",
    "authDomain": "dell-ad73e.firebaseapp.com",
    "databaseURL": "https://dell-ad73e.firebaseio.com",
    "projectId": "dell-ad73e",
    "storageBucket": "dell-ad73e.appspot.com",
    "messagingSenderId": "815707311314",
    "appId": "1:815707311314:web:074032d9722c2f88b8f10b",
    "measurementId": "G-C1GDL9MYZN"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

@app.route('/output')
def _ensure_hero():
    PROJECT  = db.child('project').order_by_child("class").equal_to(prediction).limit_to_first(1).get()
    for project in PROJECT .each(): 
        print(company.val())
    #name1 = PROJECT.child("0").get()
    #if not prediction:
        #flask.abort(404)
    
    return flask.render_template("main1.html")'''
    
    
df=pd.read_csv(r"C:\Users\KIIT\Desktop\dell\results.xlsx")   
model = pickle.load(open(r"C:\Users\KIIT\Desktop\dell\model\kmeans.pkl", 'rb'))

@app.route('/')
def home():
      return(flask.render_template('search.html'))

'''@app.route('/output')
def output():
    # create a dataframe 
    dataframe = pd.DataFrame(df, columns = ['Id', 'Company', 'Product', 'TypeName','Inches',  'Cpu', 'Ram','Memory','Gpu', 'OpSys', 'Price_euros', 'Class']) 
    # selecting rows based on condition 
    rslt_df = dataframe[dataframe['Class'] == 0] 
    print('\nResult dataframe :\n', rslt_df) 
    return flask.render_template('main1.html', prediction_text='predicted should be $ {}'.format( rslt_df))'''

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
      
    
    

    return flask.render_template('output.html')
    #return flask.render_template('main1.html', prediction_text='predicted should be $ {}'.format( prediction))



@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      #user = request.form['username']
      return redirect(url_for('predict'))
   
      

@app.route("/signup", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['username']
        passw = request.form['psw']
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("/login"))
    return flask.render_template("login.html")

      


if __name__ == '__main__':
    app.run(debug = True)