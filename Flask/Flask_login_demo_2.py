# Sample code to check if login with remember me functionality and fresh login is working correctly
# Fresh login means if we close the browser and then reopen it , it will prompt us to login again since even though the remember me token has not expired, since we have closed the browser the freshness is not retained.
# So unless we close the browser nothing is checked . The session duration is also not checked and the freshness is also not checked.
# Once we close the browser and then open it back again , if we just go to the protected route then if the session duration has not passed then it would load as normal but if the time has passed we have to login back again

#If we change the database password in the meantime then as soon as we change the password and refresh the page then the original token gets invalidated even if the remember me is active


from flask import Flask,render_template,request,flash,session,redirect
from flask_login import LoginManager,UserMixin,login_user,login_required,current_user,logout_user,fresh_login_required
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlparse,urljoin
from itsdangerous import URLSafeSerializer
from datetime import timedelta
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server

app = Flask(__name__)
app.config['SECRET_KEY'] = "This is a secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
# Even though the user checks the remember me functionality the session should time out after 60 secs
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=60)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please login to access this page"
login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = 'You need to login again'

serializer = URLSafeSerializer(app.secret_key)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command("runserver",Server(
    use_debugger = True,
    use_reloader  = True,
    host = '0.0.0.0',
    port = 5000
))


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
    user.password = 'dimpi'
    user.session_token = serializer.dumps(['Subhayan','rahul'])
    db.session.commit()
    
    
@login_manager.user_loader
def load_user(session_token):
    user = User.query.filter_by(session_token=session_token).first()
    return user
    
    
@app.route('/login',methods=['GET','POST'])
def login():
    if '_fresh' in session:
        if not session['_fresh']:
            print ("Message from login route : This session is not fresh")
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        value = request.form.getlist('remember')
        user = User.query.filter_by(username=username,password=password).first()
        if user:
            if len(value) == 0:
                login_user(user)
            else:
                login_user(user,remember=True)
            if 'next' in session:
                next = session['next']
                if is_safe_url(next) and next:
                    return redirect(next)
            return "You are now logged in !"
        else:
            flash("No such user")
    session['next'] = request.args.get('next')
    if not session['next']:
        if current_user.is_authenticated:
            return "User {} is already logged in".format(current_user.username)
    else:
        if current_user.is_authenticated:
            print ("Even though current user is : {} authenticated".format(current_user.username))
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
    
@app.route('/fresh')
@fresh_login_required
def fresh():
    if session['_fresh']:
        print ("Message from fresh route : session is fresh")
    return "<h1>You have a fresh session</h1>"
    

if __name__ == "__main__":
    manager.run()
