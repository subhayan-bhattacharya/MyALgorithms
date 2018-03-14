from flask import Flask,request,jsonify
import requests
from werkzeug.exceptions import InternalServerError, NotFound

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret!"

proxies = {
  'http': 'http://www-proxy.us.oracle.com:80',
  'https': 'http://www-proxy.us.oracle.com:80',
}


@app.errorhandler(InternalServerError)
def internal_error(error):
    return jsonify({'status':'HTTPError'})


@app.route('/test/<int:code>',methods=['GET'])
def test(code):
    url = 'https://httpbin.org/status/' + str(code)
    print "Sending to URL : {}".format(url)
    r = requests.get(url,proxies=proxies)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        raise InternalServerError
        
    return jsonify({'status':'Success'})
        

if __name__ == '__main__':
    app.run(debug=True)