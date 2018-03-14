from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,RadioField,SelectField
from wtforms.validators import InputRequired,Email

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret!"

class MyForm(FlaskForm):
    email = StringField('Email',validators=[InputRequired(),Email()])
    password = PasswordField('Password',validators=[InputRequired()])
    textarea = TextAreaField('Textarea')
    radiofield = RadioField('Radio',default='Option one',choices=[('Option one','Option one is this'),('Option2','Option2 is this')])
    selects = SelectField('Selects',choices=[('1','1'),('2','2'),('3','3')])
    
@app.route('/',methods=['GET','POST'])
def home():
    form = MyForm()
    return render_template('start.html',form=form)
    
if __name__ == '__main__':
    app.run(debug=True)