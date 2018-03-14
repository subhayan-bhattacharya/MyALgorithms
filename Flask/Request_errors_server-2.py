from flask import Flask,request,jsonify
import requests
from werkzeug.exceptions import InternalServerError, NotFound

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret!"


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'status':'500'})
    
    
@app.errorhandler(404)
def internal_error(error):
    return jsonify({'status':'404'})


@app.route('/test/<int:code>',methods=['GET'])
def test(code):
    url = 'https://httpbin.org/status/' + str(code)
    print "Sending to URL : {}".format(url)
    r = requests.get(url,proxies=proxies)
    
    if r.status_code == 500:
        raise InternalServerError
    elif r.status_code == 404:
        raise NotFound
    else:
        return jsonify({'status':'Success'})
        

if __name__ == '__main__':
    app.run(debug=True)