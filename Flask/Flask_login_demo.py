from flask import Flask,render_template,request,flash,session,redirect
from flask_login import LoginManager,UserMixin,login_user,login_required,current_user,logout_user
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlparse,urljoin
from itsdangerous import URLSafeTimedSerializer,SignatureExpired
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = "This is a secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please login to access this page"

serializer = URLSafeTimedSerializer(app.secret_key)

db = SQLAlchemy(app)

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url,target))
    return test_url.scheme in ('http','https') and ref_url.netloc == test_url.netloc


class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(30))
    session_token = db.Column(db.String(100),unique=True)
    
    def get_id(self):
        return str(self.session_token)
        
        
def create_user():
    user = User(username="Subhayan",password="test",session_token=serializer.dumps(['Subhayan','test']))
    db.session.add(user)
    db.session.commit()
    
def update_token():
    user = User.query.filter_by(username="Subhayan").first()
    user.password = 'test321'
    user.session_token = serializer.dumps(['Subhayan','some'])
    db.session.commit()
    
    
@login_manager.user_loader
def load_user(session_token):
    user = User.query.filter_by(session_token=session_token).first()
    try:
        serializer.loads(session_token,max_age=60)
    except SignatureExpired:
        return None
        
    return user
   
    
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if user:
            session_token = serializer.dumps(['Subhayan','test'])
            user.session_token = session_token
            db.session.commit()
            
            login_user(user,remember=True)
            if 'next' in session:
                next = session['next']
                if is_safe_url(next) and next:
                    return redirect(next)
            return "You are now logged in !"
        else:
            flash("No such user")
    session['next'] = request.args.get('next')
    print (session['next'])
    return render_template('login.html')
    
@app.route('/home')
@login_required
def home():
    return "<h1>You are in the protected area {} </h1>".format(current_user.username)
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "<h1>Logged out !</h1>"
    

if __name__ == "__main__":
    app.run(debug=True)