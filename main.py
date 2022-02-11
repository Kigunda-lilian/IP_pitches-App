from unicodedata import name
from flask import Flask, redirect, render_template ,request, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LogInForm,SignupForm,PitchesForm,CommentsForm,UpdateProfileForm
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from werkzeug.security import check_password_hash,generate_password_hash
from flask_bootstrap import Bootstrap

from models.user import User
from models.comments import Comments
from models.pitches import Pitches

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

@app.route("/",methods = ["GET","POST"])#view function
def home():
   return render_template('index.html')


#login
@app.route('/login',methods = ["GET","POST"])
def login():
    
    form=LogInForm()
    
    #check for validation
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        
        if user:
            #compare the passwords
            if check_password_hash(user.password,form.password):
                login_user(user)
                return redirect(url_for("pitches"))
            print("Invalid username or password")
        print("Invalid username or password")
       
    return render_template("login.html",registration_form=form)


#signup
@app.route('/signup',methods = ["GET","POST"])
def signup():
    
    form = SignupForm()
    
    if form.validate_on_submit():
        First_name = form.First_name.data
        Last_name = form.Last_name.data
        username = form.username.data
        email= form.email.data
        password =form.password.data
        confirm_password = form.confirm_password.data
        # remember_me = form.remember_me.data
        # submit = form.submit.data
        
        # Hash password
        hashed_password = generate_password_hash(password,method="sha256")
        
        new_user=User(First_name = First_name,Last_name=Last_name,username=username,email=email,password=hashed_password,confirm_password=hashed_password)
        
        #send data to db
        db.session.add(new_user)
        db.session.commit
        print("User has been added successfully")
        return redirect (url_for('login'))
    
    return render_template("signup.html",registerform=form)


#logout
@app.route('/logout')
def logout():
    return redirect (url_for('home'))

# #comments
@app.route('/comments',methods = ["GET","POST"])
@login_required
def comments():
    
    form = CommentsForm()
    
    return render_template("comments.html",feedbackform=form,name=current_user.username)


# #pitches
@app.route('/pitches',methods = ["GET","POST"])
@login_required
def pitches():
    
    form = PitchesForm()
    
    return render_template("pitch.html",pitchform=form,name=current_user.username)




if __name__ == '__main__':
    app.run(debug=True)
