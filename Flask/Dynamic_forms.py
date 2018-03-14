import json
from flask import Flask,render_template,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,BooleanField,Form,FormField,FieldList,ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecret!'

@app.route('/DisplayForm/<form_type>')
def display_form(form_type):
	class_attrs = {}
	display_str = "<h1>"
	for key,value in data[form_type].items():
		if value == "text":
			dict_str = "class_attrs[\"{}\"] = StringField(validators=[InputRequired()])".format(key)
			exec(dict_str)
		elif value == "int":
			dict_str = "class_attrs[\"{}\"] = IntegerField(validators=[InputRequired()])".format(key)
			exec(dict_str)
	
	#Create form class
	cls_create_str = "{} = type(\"{}\",(FlaskForm,),class_attrs)".format(form_type,form_type)
	exec(cls_create_str)
	
	#Instantiate the form class
	instantiate_cls_str = "form = {}()".format(form_type)
	exec(instantiate_cls_str)
	
	if form_type == "UserDetails":
		return render_template('UserDetails.html',form=form)
	else:
		return render_template('UserAddress.html',form=form)

			
@app.route('/DisplayDetails',methods=["POST"])
def display_details():
    display_str = "<h1>"
    for field in request.form.keys():
		display_str += "Field : {} and value : {}".format(field,request.form[field])
		display_str += "<br>"
    display_str += "</h1>"
	
    return display_str
		
if __name__ == "__main__":

	with open('sample.json','r') as f:	
		data = json.load(f)
	
	app.run(debug=True)