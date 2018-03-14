from flask import Flask,render_template,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,BooleanField,Form,FormField,FieldList,ValidationError
from wtforms.validators import InputRequired
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecret!'

@app.route('/Dynamic/<string:form_type>',methods=['GET','POST'])
def dynamic(form_type):

    class DynamicForm(FlaskForm):
        pass
    for key,value in data[form_type].items():
        if value == "text":
            exec_str = "DynamicForm.{} = StringField(\'{}\',validators=[InputRequired()])".format(key,key)
            exec(exec_str)
        elif value == "int":
            exec_str = "DynamicForm.{} = IntegerField(\'{}\',validators=[InputRequired()])".format(key,key)
            exec(exec_str)
            
    form = DynamicForm()
    if form.validate_on_submit():
        if form_type == "UserDetails":
            return "<h1> Name : {} and Lastname : {} and Age : {}</h1>".format(form.Name.data,form.LastName.data,form.Age.data)
        else:
            return "<h1>City : {} and State: {} and Country : {}".format(form.City.data,form.State.data,form.Country.data)
            
    if form_type == "UserDetails":
        return render_template('UserDetails.html',form=form)
    else:
        return render_template('UserAddress.html',form=form)
    

if __name__ == "__main__":
    with open('sample.json','r') as f:
        data = json.load(f)
    app.run(debug=True)