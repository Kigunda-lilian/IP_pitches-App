from flask import Flask, render_template ,request, url_for
from flask_sqlalchemy import sqlalchemy
from forms import LogInForm,SignupForm,PitchesForm,CommentsForm,UpdateProfileForm

#  import cofigs
from configs.base_config import *

#create an instance of my app
app = Flask(__name__)

#specify my db environment
app.config.from_object(Development)

# create my sqlAlchemy instance


#application endpoint
# create my decorator ..> route
@app.route("/")
#view function
def home():
    return render_template('index.html')


#login
@app.route('/login')
def login():
    
    form=LogInForm
       
    return render_template("login.html",form=form)


#signup
@app.route('/signup')
def signup():
    
    form = SignupForm
    
    return render_template("signup.html",form=form)


#logout
@app.route('/logout')
def logout():
    return render_template("logout.html")

#comments
@app.route('/comments')
def comments():
    
    form = CommentsForm
    
    return render_template("comments.html",form=form)


#pitches
@app.route('/pitches')
def pitches():
    
    form = PitchesForm
    
    return render_template("pitch.html",form=form)




if __name__ == '__main__':
    app.run(debug=True)
