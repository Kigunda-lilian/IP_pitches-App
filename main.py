from flask import Flask, render_template
from flask_sqlalchemy import sqlalchemy

#create an instance of my app
app=Flask(__name__)

# create my sqlAlchemy instance


#application ednpoint
# create my decotaror ..> route
@app.route("/")
#view function
def home():
   return render_template("index.html")

#login
@app.route('/login')
def login():
       return render_template("login.html")

#signup
@app.route('/signup')
def signup():
       return render_template("signup.html")

#logout
@app.route('/logout')
def logout():
       return render_template("logout.html")



if __name__=='__main__':
    app.run(debug = True)
