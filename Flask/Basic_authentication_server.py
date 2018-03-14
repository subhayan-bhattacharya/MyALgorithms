from flask import Flask,request,jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret!"
app.config['BASIC_AUTH_USERNAME'] = 'Subhayan'
app.config['BASIC_AUTH_PASSWORD'] = 'Bhattacharya'

basic_auth = BasicAuth(app)

@app.route('/test',methods=['POST'])
@basic_auth.required
def test():
    name = request.form['name']
    lastname = request.form['lastname']
    return jsonify({'name':'Response','lastname':'Bhattacharya'})
        

if __name__ == '__main__':
    app.run(debug=True)