from flask import Flask,render_template,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,BooleanField,Form,FormField,FieldList,ValidationError
from wtforms.validators import InputRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecret!'


class CompanyDetailsForm(Form):
    company_name = StringField('Company name',validators=[InputRequired()])
    location = StringField('Location',validators=[InputRequired()])
    

class IndexForm(FlaskForm):
    no_of_companies = IntegerField('No of companies worked so far')

    def validate_no_of_companies(form,field):
        if field.data > 5:
            raise ValidationError("No of companies cannot be more than 5")

@app.route('/CompanyDetails/<int:num_com>',methods=["GET","POST"])
def company_details(num_com):

    class CompanyForm(FlaskForm):
        first_name = StringField('First Name',validators=[InputRequired()])
        companies = FieldList(FormField(CompanyDetailsForm),min_entries=num_com)
	
    form = CompanyForm()
	
    if request.method == "POST" and form.validate_on_submit():
		display_str = "<h1>"
		for field in request.form.keys():
			if field != "csrf_token":
				display_str += "Field = {} and value : {}".format(field,request.form[field])
				display_str += "<br>"
		display_str += "</h1>"
		
		return display_str
			
    return render_template('Companies.html',form=form)
	

@app.route('/home',methods=["GET","POST"])
def home():
    form = IndexForm()
    if form.validate_on_submit():
        return redirect(url_for('company_details',num_com=form.no_of_companies.data))
    return render_template('home.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)