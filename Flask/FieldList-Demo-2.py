from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,BooleanField,Form,FormField,FieldList
from wtforms.validators import InputRequired,Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Subhayan'

class TelephoneForm(Form):
    country_code = IntegerField('Country code')
    area_code = IntegerField('Area code')
    number = StringField('Number')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    first_name = StringField('First Name',validators=[InputRequired()])
    last_name = StringField('Last Name',validators=[InputRequired()])
    age = IntegerField('Age')
    male = BooleanField('Male')
    email = StringField('Email',validators=[Email()])
    phone_number = FieldList(FormField(TelephoneForm))

    
class User:
    def __init__(self,username,age,email,male=True):
        self.username = username
        self.age = age
        self.email = email
        self.male = male
    
@app.route('/index',methods=['GET','POST'])
def index():

    p1 = {'country_code':91,'area_code':33,'number':"26528745"}
    p2 = {'country_code':91,'area_code':33,'number':"9830823119"}
    
    phones = {'phone_number':[p1,p2]}  
  
    user = User('subhayan_here',33,'subhayan.here@gmail.com',False)
   
    form = LoginForm(obj=user,data=phones)
    
    #del form.email
    
    if form.validate_on_submit():
        # return """
        # <h1>
        # <ol>
            # <li> Username : {} </li>
            # <li> Password : {} </li>
            # <li> Age: {} </li>
            # <li> First Name: {} </li>
            # <li> Last Name : {} </li>
            # <li> Male : {} </li>
        # """.format(form.username.data,form.password.data,form.age.data,form.first_name.data,form.last_name.data,form.male.data)
        #return "<h1>Country code : {} and area code is : {} and the number is : {}".format(form.phone_number.country_code.data,form.phone_number.area_code.data,form.phone_number.number.data)
        output = "<h1>"
        for ph_no in form.phone_number:
            c_code = ph_no.country_code.data
            a_code = ph_no.area_code.data
            p_no = ph_no.number.data
            output = output + "Country code : {} and area code : {} and phone number : {}".format(c_code,a_code,p_no)
        output = output + "</h1>"
        return output
            
        
    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    