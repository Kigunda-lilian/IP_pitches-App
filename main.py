from flask import Flask, redirect, render_template ,request, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LogInForm,SignupForm,PitchesForm,CommentsForm,UpdateProfileForm
from flask_login import LoginManager
from werkzeug.security import check_password_hash,generate_password_hash
from flask_bootstrap import Bootstrap
# from user import User
# from models.comments import Comments
# from models.pitches import Pitches
# from models.user import User
#  import cofigs
from configs.base_config import *

#create an instance of my app
app = Flask(__name__)

#specify my db environment
app.config.from_object(Development)

# create my sqlAlchemy instance
db =SQLAlchemy(app)
bootstrap = Bootstrap(app)

#create auth instance

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
 




@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

#application endpoint
# create my decorator ..> route

@app.route("/")#view function
def home():
   return render_template('index.html')


#login
@app.route('/login',methods = ["GET","POST"])
def login():
    
    form=LogInForm()
    
    #check for validation
    # if form.validate_on_submit():
    #     user=User.query.filter_by(username=form.username.data)
        
        
       
    return render_template("login.html",registration_form=form)


#signup
@app.route('/signup',methods = ["GET","POST"])
def signup():
    
    form = SignupForm()
    
    return render_template("signup.html",registerform=form)


#logout
@app.route('/logout')
def logout():
    return redirect (url_for('home'))

# #comments
@app.route('/comments')
def comments():
    
    form = CommentsForm()
    
    return render_template("comments.html",feedbackform=form)


# #pitches
@app.route('/pitches')
def pitches():
    
    form = PitchesForm()
    
    return render_template("pitch.html",pitchform=form)




if __name__ == '__main__':
    app.run(debug=True)
