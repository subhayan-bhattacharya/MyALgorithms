from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,RadioField,BooleanField
from wtforms_components import SelectField,SelectMultipleField
from wtforms.validators import InputRequired,Email


app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret!"

def get_radio_choices():
    choices = [
    ('Single',
        (
            ('1','Single car'),
        )
    ),
    ('Multiple',
        (
            ('2','Two cars'),
            ('3','Three cars')
        )
    ),
    ('None','No car'),
    ('Bike','Only bikes')
    ]
    
    return choices
        
def get_bike_choices():
    choices = [
    ('Gifted',
        (
            ('Washing machine','Washing machine'),
            ('Microwave','Microwave oven')
        )
    ),
    ('Default',
        (
            ('Geyser','Geyser'),
        )
    ),
    ('Bought',
        (
            ('Television','Television'),
        )
    )
    ]
    
    return choices
        

class MyForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    details = TextAreaField('Details')
    sex = RadioField('Sex',default='Male',choices=[('male','Male'),('female','Female')])
    cars = SelectField('No of cars',choices=get_radio_choices(),default='3')
    appliances = SelectMultipleField('No of appliances',choices=get_bike_choices())
    photo = FileField(validators=[FileRequired()])
    
    
@app.route('/index',methods=['GET','POST'])
def index():
    f = MyForm()
    
    if f.validate_on_submit():
        display_str = "<h1>"
        display_str += "name : {}<br>".format(f.name.data)
        display_str += "password : {}<br>".format(f.password.data)
        display_str += "details : {}<br>".format(f.details.data)
        display_str += "Cars : {} <br>".format(f.cars.data)
        display_str += "Appliances : <br>"
        for item in f.appliances.data:
            display_str += "{}<br>".format(item)
        display_str += "</h1>"
        
       
        return display_str
    
    return render_template('index.html',form=f)

if __name__ == '__main__':
    app.run(debug=True)