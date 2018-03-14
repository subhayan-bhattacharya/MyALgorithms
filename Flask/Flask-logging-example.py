from flask import Flask,request,jsonify
import requests
import logging
import os
import json
import logging.config

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret!"
SITE_ROOT = os.path.dirname(os.path.realpath(os.path.dirname(__file__)))
default_path = os.path.join(SITE_ROOT, 'Practice','logging.json')

with open(default_path, 'rt') as f:
    log_config = json.load(f)
logging.config.dictConfig(log_config)
logger = logging.getLogger("ui")
app.logger.handlers = logger.handlers
app.logger.setLevel(logger.level)

proxies = {
  'http': 'http://www-proxy.us.oracle.com:80',
  'https': 'http://www-proxy.us.oracle.com:80',
}

      
       
@app.route('/test',methods=["GET","POST"])
def test():
    url = "https://httpbin.org/status/404"
    try:
        response = requests.get(url,proxies=proxies)
        if response.status_code != 200:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                status = response.status_code
                app.logger.info("New http exception")
                app.logger.info(status)
                return jsonify({"message":"HTTPError","status":status})
    except requests.exceptions.RequestException as e:
        app.logger.info("An exception has been raised")
        app.logger.info(e)
        raise InvalidUsage("request exception has been raised")
        
if __name__ == "__main__":
    app.run(debug=True)
    app.logger.addHandler('custom_handler')
    
    