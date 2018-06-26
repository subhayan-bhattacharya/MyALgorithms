# Simple demo of how a Python list can be updated using jquery.

from flask import Flask,render_template,request,jsonify
import requests

app = Flask(__name__)

fruits = ["Apple","Mango","Peach","Pineapple","jackfruit","guava","banana","cucumber"]


@app.route('/index')
def index():
    response = requests.get('http://127.0.0.1:5000/get_fruits/3')
    print (response)
    out = response.json()
    return render_template('index_2.html',fruits=out['fruits'])
    #return "Just checking"
    
@app.route('/')
def home():
    return "Home page"
    
@app.route('/get_fruits/<int:num>')
def get_fruits(num):
    global fruits
    sliced_fruits = fruits[:num]
    new_list = fruits[num:] + fruits[:num]
    fruits = new_list
    return jsonify({'fruits': sliced_fruits})



if __name__ == "__main__":
    app.run(debug=True,threaded=True)
    
    

            
        


        
        
    
        
    
    
    


